# -*- coding: utf-8 -*-

import json


class Response:

    def __init__(self, method, status, content):

        self.method = method
        self.status = status
        self.content = content

    def is_ok(self):
        return self.status and int(self.status) < 400

    def json(self):
        return self.result

    def object(self):
        return json.loads(self.content)

    def __repr__(self):
        return "%s %s" % (self.status, self.content)
