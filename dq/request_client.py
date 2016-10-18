# -*- coding: utf-8 -*-

import requests

from .response import Response


class RequestClient:

    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': 'Bearer %s' % self.token
        })

    def __make_url(self, path):
        return '{}/{}'.format(self.base_url, path)

    def __get_body(self, request, body_as_json):
        if body_as_json:
            return request.json()
        else:
            return request.text

    def get(self, path, headers={}, body_as_json=False):
        response = self.session.get(self.__make_url(path), headers=headers)
        return Response('GET', response.status_code,
                        self.__get_body(response, body_as_json))

    def post(self, path, headers={}, body_as_json=False):
        response = self.session.post(self.__make_url(path), headers=headers)
        return Response('POST', response.status_code,
                        self.__get_body(response, body_as_json))

    def put(self, path, headers={}, body_as_json=False):
        response = self.session.put(self.__make_url(path), headers=headers)
        return Response('PUT', response.status_code,
                        self.__get_body(response, body_as_json))

    def delete(self, path, headers={}, body_as_json=False):
        response = self.session.get(self.__make_url(path), headers=headers)
        return Response('DELETE', response.status_code,
                        self.__get_body(response, body_as_json))

    def post_multipart(self, path, parts={}, headers={}, body_as_json=False):
        files = {k: (v['filename'], v['content'], v['content-type'])
                 for k, v in parts.items()}
        response = self.session.post(self.__make_url(path), headers=headers,
                                     files=files)
        return Response('POST', response.status_code,
                        self.__get_body(response, body_as_json))
