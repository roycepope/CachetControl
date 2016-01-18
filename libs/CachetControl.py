"""
Created on Jan 17, 2016

@author: royce
"""

import json
import requests


class CachetControl(object):
    """
    classdocs
    """
    __token = ''
    __header = {'X-Cachet-Token': __token}

    '''
    Constructor
    '''
    def __init__(self):
        self.__prefix = "http://status.overlook.sh/api/v1/"
        pass

    '''
    Get json response for components
    '''
    def getComponenets(self):
        try:
            response = requests.get(self.__prefix + 'components', headers=self.__header)
        except requests.ConnectionError:
            raise Exception("REST Server not found!")
        json_data = json.loads(response.text)
        print json.dumps(json_data, indent=2)
        return

    '''
    Get json response for incidents
    '''
    def getIncidents(self):
        try:
            response = requests.get(self.__prefix + 'incidents', headers=self.__header)
        except requests.ConnectionError:
            raise Exception("REST Server not found!")
        json_data = json.loads(response.text)
        print json.dumps(json_data, indent=2)
        return

    '''
    Get json response for metrics
    '''
    def getMetrics(self):
        try:
            response = requests.get(self.__prefix + 'metrics', headers=self.__header)
        except requests.ConnectionError:
            raise Exception("REST Server not found!")
        json_data = json.loads(response.text)
        print json.dumps(json_data, indent=2)
        return
    '''
    Ping
    '''
    def ping(self):
        try:
            response = requests.get(self.__prefix + 'ping', headers=self.__header)
        except requests.ConnectionError:
            raise Exception("REST Server not found!")
        json_data = json.loads(response.text)['data']
        print json_data
        return

    def mumbleMonitor(self):
        try:
            response = requests.post(self.__prefix + 'metrics/2/points', data={"value": "1"}, headers=self.__header)
        except requests.ConnectionError:
            raise Exception("REST Server not found!")
        json_data = json.loads(response.text)
        return