"""
@Author: Hizaoui Mohamed Abdelkader
@Email-1: hizaoui.ma@gmail.com
@Email-2: hizaoui.mohamed.abdelkader@gmail.com
@created on: '3/5/17'
"""
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from bfm import application


if __name__ == '__main__':
    http_server = HTTPServer(application())
    http_server.bind(8080)
    try:
        http_server.start(0)
        IOLoop.current().start()
    except KeyboardInterrupt:
        IOLoop.current().stop()
    finally:
        http_server.stop()