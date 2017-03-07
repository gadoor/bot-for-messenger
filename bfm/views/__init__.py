"""
@Author: Hizaoui Mohamed Abdelkader
@Email-1: hizaoui.ma@gmail.com
@Email-2: hizaoui.mohamed.abdelkader@gmail.com
@created on: '3/5/17'
"""
import json
from tornado.web import RequestHandler


class CustomRequestHandler(RequestHandler):
    def get_rest_params(self, required=None):
        try:
            params = json.loads(self.request.body.decode())
            if required:
                missing_params = [param for param in required if not params.get(param, None)]
                if missing_params:
                    self.send_error(status_code=400,
                                    message="Missing Required Parameters In Request Body",
                                    missing_params=missing_params)
                else:
                    return params
            else:
                return params
        except Exception as e:
            self.send_error(status_code=400)

    def write_rest(self, chunk):
        if not self._finished:
            if chunk:
                self.write(chunk)
            else:
                self.send_error(status_code=404,
                                message="Requested Resource Does Not Exist")

    def write_error(self, status_code, **kwargs):
        response = {'status_code': status_code}
        try:
            response.update(kwargs)
            self.finish(response)
        except Exception as e:
            self.finish(response)