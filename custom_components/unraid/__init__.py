"""The unraid component."""

import logging
import os.path, time

# Home assistant
import voluptuous as vol
from homeassistant import config_entries
import homeassistant.helpers.config_validation as cv

# GraphQL
import requests
from requests.exceptions import Timeout
from requests.exceptions import ConnectionError

import json

# Constants
from .const import (
    DOMAIN,
    HOSTS,

    CONF_HOST,
    CONF_API_KEY,

    GRAPHQL_ENDPOINTS,
    SENSOR_LIST,
)

# Config schema
CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                vol.Required(CONF_HOST): cv.string,
                vol.Required(CONF_API_KEY): cv.string,
                # vol.Optional(CONF_BINARY_SENSOR): vol.All(
                #     cv.ensure_list, [BINARY_SENSOR_SCHEMA]
                # ),
                # vol.Optional(CONF_SENSOR): vol.All(cv.ensure_list, [SENSOR_SCHEMA]),
                # vol.Optional(CONF_SWITCH): vol.All(cv.ensure_list, [SWITCH_SCHEMA]),
            }
        )
    },
    extra=vol.ALLOW_EXTRA,
)

# Set logger name
_LOGGER = logging.getLogger(__name__)

# def setup(hass, config):
async def async_setup(hass, config):
    """Set up the Unraid component using YAML"""

    # Check config is setup
    if config.get(DOMAIN) is None:
        # We get here if the integration is set up using config flow
        return True

    # Debug log we're starting
    _LOGGER.debug("YAML Setup started")

    # Setup data dict
    hass.data[DOMAIN] = {}

    # Get "global" configuration.
    host = config[DOMAIN].get(CONF_HOST)
    api_key = config[DOMAIN].get(CONF_API_KEY)

    # Config the unRAID Client
    try:
        api = UnraidClient(
            hass, host, api_key
        )

        # Prepare JSON objects
        for sensor_name in SENSOR_LIST:
            api._json_object[sensor_name] = {}

        # Store data
        hass.data[DOMAIN] = {"config": config[DOMAIN], "api": api}

        # Load sensors
        hass.helpers.discovery.load_platform('sensor', DOMAIN, {"host": host}, config)


        # Add config Flow
        hass.async_create_task(
            hass.config_entries.flow.async_init(
                DOMAIN, context={"source": config_entries.SOURCE_IMPORT}, data={}
            )
        )
    except Exception:
        _LOGGER.error("(YAML) unRAID Fatal Error: %s - Failed to connect to API", host)

    return True

async def async_setup_entry(hass, config_entry):
    """Set up this integration using UI."""
    conf = hass.data.get(DOMAIN)
    if config_entry.source == config_entries.SOURCE_IMPORT:
        if conf is None:
            hass.async_create_task(
                hass.config_entries.async_remove(config_entry.entry_id)
            )
        return False

    # Debug log we're starting
    _LOGGER.debug("UI Setup started")

    # Create DATA dict
    hass.data[DOMAIN] = {}

    # Get "global" configuration.
    host = config_entry.data.get(CONF_HOST)
    api_key = config_entry.data.get(CONF_API_KEY)

    # _LOGGER.debug("host: %s", host)
    # _LOGGER.debug("api_key %s", api_key)

    try:

        _LOGGER.debug("(UI) Do API")

        api = UnraidClient(
            hass, host, api_key
        )

        _LOGGER.debug("(UI) Do sensors")
        for sensor_name in SENSOR_LIST:
            api._json_object[sensor_name] = {}

        _LOGGER.debug("(UI) Do data")
        hass.data[DOMAIN] = {"config": config_entry.data, "api": api}

        # Load sensors
        # _LOGGER.debug("(UI) Do load of sensors")
        # hass.helpers.discovery.load_platform('sensor', DOMAIN, {"host": host}, config_entry.data)
    except Exception:
        _LOGGER.error("(UI) unRAID Fatal Error: %s - Failed to connect to API", host)

    # Add binary_sensor
    # hass.async_add_job(
    #     hass.config_entries.async_forward_entry_setup(config_entry, "binary_sensor")
    # )
    #
    # Add sensor
    hass.async_add_job(
        hass.config_entries.async_forward_entry_setup(config_entry, "sensor")
    )
    #
    # # Add switch
    # hass.async_add_job(
    #     hass.config_entries.async_forward_entry_setup(config_entry, "switch")
    # )

    return True




class UnraidClient:
    """Handle GraphQL communications"""

    def __init__(self, hass, host, api_key):
        """Initialize the Unraid GraphQL Client."""

        self._host = host
        self._api_key = api_key

        self._hass = hass
        self._json_object = {}

    def poll_graphql(self, graphql='All'):
        # Get all sensor data
        graphql_query = ''
        if not graphql == 'All':
            graphql_query += GRAPHQL_ENDPOINTS[graphql]
        else:
            for sensor_name in SENSOR_LIST:
                graphql_query += GRAPHQL_ENDPOINTS[sensor_name] + ','

        # Make request
        try:
            _LOGGER.debug("Host = %s", self._host)

            # Dump the request query
            _LOGGER.debug('Request GraphQL = %s', graphql)
            _LOGGER.debug('Request = {%s}', graphql_query)

            result = requests.post(
                self._host + '/graph',
                headers = {
                    'x-api-key': self._api_key,
                },
                json = {
                    'query': '{'+ graphql_query +'}',
                },
            )

            json_result = json.loads(result.content)

            # Debug of JSON result
            _LOGGER.debug("Result = %s", json_result)

            # Process JSON
            if not graphql == 'All':
                self._json_object[graphql] = {
                    'json': json_result['data'][graphql],
                    'data': flatten_json(json_result['data'][graphql])
                }
            else:
                for sensor_name in SENSOR_LIST:
                    self._json_object[sensor_name] = {
                        'json': json_result['data'][sensor_name],
                        'data': flatten_json(json_result['data'][sensor_name])
                    }

            return self._json_object

        except Timeout:
            _LOGGER.debug('The request timed out')
        except ConnectionError as ce:
            _LOGGER.debug('Connection Error =  %s', ce)
        else:
            _LOGGER.debug('The request did not time out')

        return self._json_object


def flatten_json(y, prefix=""):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y, prefix)
    return out
