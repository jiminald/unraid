"""Platform for sensor integration."""

import logging
import asyncio

from homeassistant.helpers.entity import Entity

#from jinja2 import Template
from homeassistant.helpers import template

from .const import (
    DOMAIN,
    HOSTS,

    SENSOR_LIST,
    SENSOR_BASIC_LIST,

    SENSOR_GRAPHQL_STATES,
    SENSOR_GRAPHQL_BASIC,
)

_LOGGER = logging.getLogger(__name__)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
# def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the sensor platform."""
    # We only want this platform to be set up via discovery.
    if discovery_info is None:
        return

    sensors = []

    for sensor in [UnraidSensor(hass.data[DOMAIN], sensor_name) for sensor_name in SENSOR_LIST]:
        sensors.append(sensor)

    for sensor in [UnraidBasicSensor(hass.data[DOMAIN], sensor_name) for sensor_name in SENSOR_BASIC_LIST]:
        sensors.append(sensor)

    async_add_entities(sensors, True)
    # add_entities(sensors, True)

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Setup sensor platform."""
    sensors = []

    for sensor in [UnraidSensor(hass.data[DOMAIN], sensor_name) for sensor_name in SENSOR_LIST]:
        sensors.append(sensor)

    for sensor in [UnraidBasicSensor(hass.data[DOMAIN], sensor_name) for sensor_name in SENSOR_BASIC_LIST]:
        sensors.append(sensor)

    async_add_entities(sensors, True)


class UnraidSensor(Entity):
    """Representation of a sensor."""

    def __init__(self, config, sensor_name):
        """Initialize the sensor."""
        self._state = None
        self._result = { "json": {}, "data": "" }

        # Announce sensor
        _LOGGER.debug("Initializing sensor: %s", sensor_name)
        _LOGGER.debug("Config: %s", config)

        # Store config and the API connection
        self._name = sensor_name
        self._config = config
        self.api = config['api']
        self._condition = sensor_name

        _LOGGER.debug("Config: %s", self._config)

    @property
    def name(self):
        """Return the name of the sensor."""
        return "unraid_{}".format(self._name)

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def device_state_attributes(self):
        """Return the state attributes of the data."""
        return self._result['data']

    def update(self):
        """Get the latest data from the API."""
        self.do_update()

    async def async_update(self):
        """Get the latest data from the API."""
        self.api.poll_graphql(self._condition)
        self.do_update()


    def do_update(self):
        """Fetch new state data for the sensor."""
        self._result = self.api._json_object[self._condition]
        self._state = self.graphql_state()

    # Get state for a GraphQL Endpoint
    def graphql_state(self):
        # Get State Parameters
        state = SENSOR_GRAPHQL_STATES[self._condition]

        # Are we looking for a specific field
        if (state['field'] != ''):
            field = state['field']

            # How do we parse the data
            if (state['action'] == 'latest'):
                sensor_state = len(self._result['json']) - 1
            elif (state['action'] == 'count'):
                if (self._result['json'][field] is not None):
                    sensor_state = len(self._result['json'][field])
                else:
                    sensor_state = "0"
            else:
                sensor_state = self._result['data'][field]
        else:
            # How do we parse the data
            if (state['action'] == 'count'):
                if (self._result['json'] != 'null'):
                    sensor_state = len(self._result['json'])
                else:
                    sensor_state = "0"
            else:
                sensor_state = "N/A"

        return sensor_state


class UnraidBasicSensor(Entity):
    """Representation of a sensor."""

    def __init__(self, config, sensor_name):
        """Initialize the sensor."""
        self._state = None
        self._result = None

        # Announce sensor
        _LOGGER.debug("Initializing basic sensor: %s", sensor_name)

        # Store config and the API connection
        self._config = config
        self.api = config['api']

        self._name = sensor_name

        self._config['basic'] = SENSOR_GRAPHQL_BASIC[sensor_name]
        self._config['sensor_name'] = sensor_name
        self._condition = self._config['basic']['graphql_endpoint']

        # Show config
        _LOGGER.debug("(%s) Config: %s", sensor_name, self._config)

    @property
    def name(self):
        """Return the name of the sensor."""
        return "unraid_{}".format(self._name)

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def device_state_attributes(self):
        """Return the state attributes of the data."""
        if ("attributes" in self._config['basic']):
            return self._config['basic']['attributes']
        else:
            return None

    def update(self):
        """Get the latest data from the API."""
        self.do_update()

    async def async_update(self):
        """Get the latest data from the API."""
        self.api.poll_graphql(self._condition)
        self.do_update()

    def do_update(self):
        """Fetch new state data for the sensor."""

        # Refetch config
        self._config['basic'] = SENSOR_GRAPHQL_BASIC[self._name]

        # Get data
        _result = self.api._json_object[self._condition]

        # Render output
        try:
            self._temp = template.Template(
                self._config['basic']['value'], self.hass
            )
            self._state = self._temp.async_render(_result=_result)
        except Exception as exception:
            self._state = self._state
