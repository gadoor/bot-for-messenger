"""
@Author: Hizaoui Mohamed Abdelkader
@Email-1: hizaoui.ma@gmail.com
@Email-2: hizaoui.mohamed.abdelkader@gmail.com
@created on: '3/7/17'
"""
from bfm.views import CustomRequestHandler


class Index(CustomRequestHandler):
    def get(self):
        self.write("Index")
