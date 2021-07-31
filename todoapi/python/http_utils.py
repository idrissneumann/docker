from flask import request

class HttpUtils():
    def get_json_body(self):
        return request.get_json()
