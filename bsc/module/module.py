from bsc.module.client import Client
from bsc.module.model.url_builder import UrlBuilder


class Module(Client):

    def __init__(self):
        Client.__init__(self)
        self.url_builder = UrlBuilder()

    def set_module_parameters(self):
        pass
