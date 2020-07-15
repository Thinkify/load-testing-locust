"""
Test File where the tasks are specified for the HTTPUser class 'GeneralTests'.
"""

import json

from locust import SequentialTaskSet, task

import packages.locust_util as utility
import packages.models as model
import packages.requests_handler as http_request


class GeneralRequests(SequentialTaskSet):
    """
    Sequential tasks
    """
    connection_id = []

    @task
    def login(self):
        """
        Login API task
        """
        request = model.RequestModel('LOGIN')
        response = http_request.make_post_request(self.client, request)
        if response.status_code == 200:
            response.success()
        else:
            response.failure(response.json())

    # Create connection test
    @task
    def connect_connection(self):
        """
        Connect Connection API task
        """
        request = model.RequestModel('CONNECT_CONNECTION')
        request.body["config"] = json.dumps(request.body["config"])
        response = http_request.make_post_request(self.client, request)
        if response.status_code == 200:
            response.success()
        else:
            response.failure('Connect connection failed')

    # Create connection test
    @task
    def create_connection(self):
        """
        Create Connection API task
        """
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

    @task
    def delete_connection(self):
        """
        Delete Connection API task
        """
        request = model.RequestModel('DELETE_CONNECTION')
        request.body['ids'] = json.dumps(self.connection_id)
        response = http_request.make_post_request(self.client, request)
        if response.status_code == 204:
            response.success()
        else:
            response.failure('Delete connection failed')
