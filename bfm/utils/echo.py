"""
@Author: Hizaoui Mohamed Abdelkader
@Email-1: hizaoui.ma@gmail.com
@Email-2: hizaoui.mohamed.abdelkader@gmail.com
@created on: '3/5/17'
"""
from bfm.utils.logging import logger
from bfm.utils.http_client import HTTPClient


class Echo(object):
    @classmethod
    def echo_back(cls, data):
        try:
            rid = data['entry'][0]['messaging'][0]['sender']['id']
            message = data['entry'][0]['messaging'][0]['message']['text']
            return HTTPClient.send_message(rid, message)
        except Exception as e:
            logger.error(e)
            return {}