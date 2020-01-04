"""The unraid component."""

import logging

import os.path, time

# GraphQL
import requests
from requests.exceptions import Timeout
from requests.exceptions import ConnectionError

import json

# Constants
from .const import (
    DOMAIN,
    HOSTS,

    GRAPHQL_ENDPOINTS,
    SENSOR_LIST,
)


_LOGGER = logging.getLogger(__name__)

# def setup(hass, config):
async def async_setup(hass, config):
    """Set up the Unraid component."""

    _LOGGER.debug("Setup")

    hass.data[DOMAIN] = {HOSTS: {}}

    for device in config[DOMAIN]:
        host = device['host']
        api_key = device.get('api_key')

        try:
            api = UnraidClient(
                hass, host, api_key
            )

            # api.poll_graphql('All')
            for sensor_name in SENSOR_LIST:
                api._json_object[sensor_name] = {}

            hass.data[DOMAIN][HOSTS][host] = {"config": device, "api": api}


            # Load sensors
            hass.helpers.discovery.load_platform('sensor', DOMAIN, {"host": host}, config)
        except api_error:
            _LOGGER.error("UnRAID %s error %s", host, api_key)
            continue

    if not hass.data[DOMAIN][HOSTS]:
        return False

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
                # self._json_object[graphql] = flatten_json(json_result['data'][graphql])

                self._json_object[graphql] = {
                    # 'count': len(json_result['data'][graphql].keys()),
                    'json': json_result['data'][graphql],
                    'data': flatten_json(json_result['data'][graphql])
                }
            else:
                for sensor_name in SENSOR_LIST:
                    self._json_object[sensor_name] = {
                        # 'count': len(json_result['data'][sensor_name].keys()),
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
