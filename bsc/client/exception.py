class ClientException(Exception):
    """
    Base class for request exceptions
    Unhandled request client exception
    """

    message = None
    code = None

    def __init__(self, message=None, response=None):
        Exception.__init__(self)
        if message is not None:
            self.message = message
        self.response = response

    def __str__(self):
        return f'Message: {self.message}'


class ConnectionFailureException(ClientException):
    message = 'Connection failure or refusal'


class EmptyResponseException(ClientException):
    message = 'Empty response to request'


class NotOkResponseException(ClientException):
    message = 'Not ok response to request'


class BadRequestException(ClientException):
    message = 'Invalid request'


class BadAddressException(BadRequestException):
    message = 'Invalid address'


class InvalidApiKeyException(BadRequestException):
    message = 'Invalid API key"'
