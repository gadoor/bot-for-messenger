"""
@Author: Hizaoui Mohamed Abdelkader
@Email-1: hizaoui.ma@gmail.com
@Email-2: hizaoui.mohamed.abdelkader@gmail.com
@created on: '3/5/17'
"""
import os
import requests
from bfm.utils.logging import logger


class HTTPClient(object):
    token = os.getenv('FB_PAGE_ACCESS_TOKEN')
    url = "https://graph.facebook.com/v2.6/me/messages?access_token=%s" % token

    @classmethod
    def send_message(cls, rid, message):
        headers = {'content-type': "application/json"}
        body = {'recipient': {'id': rid},
                'message': {'text': message}}
        r = requests.post(cls.url, json=body, headers=headers)
        logger.info(r.json())
        return r.json()
