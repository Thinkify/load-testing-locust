"""Main file that defines HttpLocust classes. The generated swarm gets
divided between each class equally. The behaviour of each HttpLocust class is
defined by the task_set. The task_set classes contain the test cases that
each swarm performs. """

import sys

import locust.stats
from locust import HttpUser, between

from tests import general_tests

sys.path.append('')
locust.stats.CSV_STATS_INTERVAL_SEC = 1


class GeneralTests(HttpUser):
    """
    HTTPUser class that generates users. Behaviour of users is defines by the
    tasks attribute.
    """
    tasks = {general_tests.GeneralRequests: 1}
    host = None  # host name - IP/URL
    wait_time = between(1, 2)
