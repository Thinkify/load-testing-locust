"""
    Common util methods that are required in tests.
"""

import json
import random
import string


def get_cookie(login_req_body):
    cookie_template = 'JSESSIONID=<session_id>; clientId=<client_id>'
    # update correct key from response
    cookie_template = cookie_template.replace('<session_id>', login_req_body['detail']['J_Session_ID'])
    cookie_template = cookie_template.replace('<client_id>', login_req_body['detail']['CLIENT_ID'])
    return cookie_template


def to_json(string_data):
    string_data = string_data.replace("'", "\"")
    return json.loads(string_data)


def unique_name(size=6, chars=string.ascii_uppercase + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))



