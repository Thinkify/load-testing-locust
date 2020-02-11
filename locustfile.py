"""
Main file that defines HttpLocust classes. The generated swarm gets divided between each class equally. The behaviour of
each HttpLocust class is defined by the task_set. The task_set classes contain the test cases that each swarm performs.
"""

import os
import sys

import locust.stats
from locust import HttpLocust, between

from tests import general_tests

sys.path.append('')
locust.stats.CSV_STATS_INTERVAL_SEC = 1


class GeneralTests(HttpLocust):
    task_set = general_tests.GeneralRequests
    host = "http://172.18.96.3:8088/"
    wait_time = between(1, 5)
