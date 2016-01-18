"""
Created on Jan 17, 2016

@author: royce
"""

import json
import libs.requests as requests


class CachetControl(object):
    """
    classdocs
    """
    __url = 'http://status.overlook.sh'
    __token = ''
    __header = {'X-Cachet-Token': __token}
    __operational = 1
    __issues = 2
    __partial = 3
    __major = 4

    '''
    Constructor
    '''
    def __init__(self):
        self.__prefix = self.__url + "/api/v1/"
        if not self.ping():
            raise Exception("No Response from {0}".format(self.__url))
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
    Get json response for subscribers
    '''
    def getSubscribers(self):
        try:
            response = requests.get(self.__prefix + 'subscribers', headers=self.__header)
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
        if response.status_code == 200:
            json_data = json.loads(response.text)['data']
            return True
        return False

    def mumbleMonitor(self):
        try:
            response = requests.post(self.__prefix + 'metrics/2/points', data={"value": "1"}, headers=self.__header)
        except requests.ConnectionError:
            raise Exception("REST Server not found!")
        json_data = json.loads(response.text)
        return