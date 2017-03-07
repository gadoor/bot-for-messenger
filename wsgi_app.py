"""
@Author: Hizaoui Mohamed Abdelkader
@Email-1: hizaoui.ma@gmail.com
@Email-2: hizaoui.mohamed.abdelkader@gmail.com
@created on: '3/5/17'
"""
from tornado.wsgi import WSGIAdapter
from bfm import application

app = WSGIAdapter(application())
