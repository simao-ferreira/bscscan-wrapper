import requests

from bsc.modules.url_helper import UrlBuilder


class Client(UrlBuilder):

    def __init__(self, api_key):
        UrlBuilder.__init__(self, api_key)
        self.http = requests.session()

    def connect(self):
        try:
            print(self.url)
            request = self.http.get(self.url)
        except requests.exceptions.ConnectionError:
            raise Exception

        if request.status_code == 200:
            response = request.json()
            # print(response)
            if response.get('status') == '1':
                return response
            if response.get('jsonrpc') is not None:
                return response
            else:
                raise Exception(response.get('message', 'No message was found!'))
        else:
            print("Response status: %s" % request.status_code)
