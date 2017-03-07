"""
@Author: Hizaoui Mohamed Abdelkader
@Email-1: hizaoui.ma@gmail.com
@Email-2: hizaoui.mohamed.abdelkader@gmail.com
@created on: '3/5/17'
"""
from bfm.views import CustomRequestHandler
from bfm.utils.logging import logger
from bfm.utils.echo import Echo


class Callback(CustomRequestHandler):
    def get(self, *args, **kwargs):
        hub_challenge = self.get_argument("hub.challenge")
        self.write(hub_challenge)

    def post(self, *args, **kwargs):
        params = self.get_rest_params()
        logger.info(params)
        self.write_rest(Echo.echo_back(params))

    def put(self, *args, **kwargs):
        params = self.get_rest_params()
        logger.info(params)