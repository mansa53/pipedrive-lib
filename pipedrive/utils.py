import json
class Utils(object):
    def __init__(self, client):
        self._client = client
    def getPersonDetails(self,data):
        response = {}
        response['Action'] = data['meta']['action']
        response['SIQ Stop'] = 'True' if data['current']['1d49338625a9066d827b531176c589959de0a595'] == 12 else 'False'
        response['details'] = data['current']
        json.dumps(response)
        return response