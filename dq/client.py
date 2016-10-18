# -*- coding: utf-8 -*-

import json

from .request_client import RequestClient


class DQClient:

    def __init__(self, url, user, token, port=9001, api_ver='v1'):
        self.url = '{}/api/{}'.format(url, api_ver)
        self.port = port
        self.user = user
        self.token = token
        self.request_client = RequestClient(self.url, self.token)

    def list_jobs(self):
        # GET 'https://app.dataquality.pl/api/v1/jobs'
        return self.request_client.get('/jobs')

    def submit_job(self, config, input_data=None, input_file=None,
                   input_file_encoding='utf-8'):
        # POST 'https://app.dataquality.pl/api/v1/jobs'
        parts = {
            'config': {
                'filename': None,
                'content-type': 'application/json',
                'content': json.dumps(config)
            },
            'file': {
                'filename': 'tmp.csv',
                'content-type': 'text/csv',
            }
        }
        if input_data:
            parts['file']['content'] = str(input_data)
        else:
            parts['file']['content'] = open(input_file, 'r',
                                            encoding=input_file_encoding)

        return self.request_client.post_multipart('/jobs', parts=parts)

    def job_status(self, job_id):
        # GET 'https://app.dataquality.pl/api/v1/jobs/{{job_id}}/status'
        return self.request_client.get('/jobs/{}/status'.format(job_id))

    def job_result(self, job_id):
        # GET 'https://app.dataquality.pl/api/v1/jobs/{{job_id}}'
        return self.request_client.get('/jobs/{}'.format(job_id))

    def job_result_data(self, job_id, out_file=None):
        # GET 'https://app.dataquality.pl/api/v1/jobs/{{job_id}}/result'
        response = self.request_client.get('/jobs/{}/result'.format(job_id))
        if out_file:
            try:
                file = open(out_file, 'w')
                file.write(response.content)
                file.close()
            except OSError:
                print("No such file or directory.")

        return response

    def delete_job(self, job_id):
        # DELETE 'https://app.dataquality.pl/api/v1/jobs/{{job_id}}'
        return self.request_client.delete('/jobs/{}'.format(job_id))

    def stop_job(self, job_id):
        # PUT 'https://app.dataquality.pl/api/v1/jobs/{{job_id}}/stop'
        return self.request_client.put('/jobs/{}/stop'.format(job_id))

    def account_status(self):
        # GET 'https://app.dataquality.pl/api/v1/account/status'
        return self.request_client.get('/account/status')
