"""
@Author: Hizaoui Mohamed Abdelkader
@Email-1: hizaoui.ma@gmail.com
@Email-2: hizaoui.mohamed.abdelkader@gmail.com
@created on: '3/5/17'
"""
from tornado.web import Application
from bfm.views.callback import Callback


def application():
    app = Application([
        (r"/callback", Callback),
    ])
    return app