"""Platform for sensor integration."""

import logging
import asyncio

from homeassistant.helpers.entity import Entity

from .const import (
    DOMAIN,
    HOSTS,
    SENSOR_LIST,
)

_LOGGER = logging.getLogger(__name__)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
# def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the sensor platform."""
    # We only want this platform to be set up via discovery.
    if discovery_info is None:
        return

    sensors = []
    for unraid_config in hass.data[DOMAIN][HOSTS].values():
        for sensor in [
            UnraidDiskSensor(unraid_config, sensor_name) for sensor_name in SENSOR_LIST
        ]:

            sensors.append(sensor)

    async_add_entities(sensors, True)
    # add_entities(sensors, True)


class UnraidDiskSensor(Entity):
    """Representation of a sensor."""

    def __init__(self, config, sensor_name):
        """Initialize the sensor."""
        self._state = None
        self._result = None

        _LOGGER.debug("Initializing sensor: %s", sensor_name)

        self.config = config

        # self._name = 'unraid'#config['config']['host']
        self._condition = sensor_name

        # API
        self.api = config['api']


    @property
    def name(self):
        """Return the name of the sensor."""
        # return f"UnRAID {self._condition}"
        return "unraid_"+self._condition

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def device_state_attributes(self):
        """Return the state attributes of the data."""
        return self._result

    def do_update(self):
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """

        # _LOGGER.debug('DEBUG DEBUG DEBUG %s', self.api.poll_graphql(self._condition))

        self._state = "notifying"
        self._result = self.api._json_object[self._condition]

    def update(self):
        """Get the latest data from the API."""
        self.do_update()

    async def async_update(self):
        """Get the latest data from the API."""
        self.api.poll_graphql(self._condition)
        self.do_update()
