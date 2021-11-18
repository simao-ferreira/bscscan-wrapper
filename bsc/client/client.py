import requests

from bsc.client.exception import NotOkResponseException, ConnectionFailureException


class Client:

    def __init__(self):
        self.http = requests.session()

    def connect(self, url):
        try:
            print(url)
            request = self.http.get(url)
        except requests.exceptions.ConnectionError:
            raise ConnectionFailureException()
            # //TODO: Test

        if request.status_code == 200:
            response = request.json()
            # print(response)
            if response.get('status') == '1':
                return response
            if response.get('jsonrpc') is not None:
                return response
            else:
                raise NotOkResponseException(response.get('result'))
        else:
            # BadRequestException(request.status_code) //TODO: Test
            print("Response status: %s" % request.status_code)
