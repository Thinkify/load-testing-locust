"""
    Test File where the tests have to be written.
"""

from locust import TaskSequence, seq_task

import json
import packages.locust_util as utility
import packages.models as model
import packages.requests_handler as http_request


class GeneralRequests(TaskSequence):
    connection_id = []

    @seq_task(1)
    def login(self):
        request = model.RequestModel('LOGIN')
        response = http_request.make_post_request(self.client, request)
        if response.status_code == 200:
            response.success()
        else:
            response.failure(response.json())

    # Create connection test
    @seq_task(2)
    def connect_connection(self):
        request = model.RequestModel('CONNECT_CONNECTION')
        request.body["config"] = json.dumps(request.body["config"])
        response = http_request.make_post_request(self.client, request)
        if response.status_code == 200:
            response.success()
        else:
            response.failure('Connect connection failed')

    # Create connection test
    @seq_task(3)
    def create_connection(self):
        request = model.RequestModel('CREATE_CONNECTION')
        request.body['name'] = utility.unique_name()
        request.body["metadata"] = json.dumps(request.body["metadata"])
        self.connection_id = []
        response = http_request.make_post_request(self.client, request)
        print(response.content)
        if response.status_code == 200:
            self.connection_id = [(response.json()['header']['id'])]
            response.success()
        else:
            response.failure('Create connection failed')

    @seq_task(4)
    def delete_connection(self):
        request = model.RequestModel('DELETE_CONNECTION')
        request.body['ids'] = json.dumps(self.connection_id)
        response = http_request.make_post_request(self.client, request)
        if response.status_code == 204:
            response.success()
        else:
            response.failure('Delete connection failed')

