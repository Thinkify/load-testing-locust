"""
    Defines all types of HTTP methods required for tests.
"""


def make_post_request(request_object, request_data):
    """
    Parameters
    ----------
    request_object
    request_data
    Returns
    -------
    response of post call
    """
    with request_object.post(request_data.endpoint,
                             headers=request_data.headers,
                             data=request_data.body,
                             catch_response=True, verify=False) as response:
        return response


def make_get_request(request_object, request_data):
    """
    Parameters
    ----------
    request_object
    request_data
    Returns
    -------
    response of get call
    """
    with request_object.get(request_data.endpoint,
                            headers=request_data.headers,
                            catch_response=True, verify=False) as response:
        return response


def make_put_request(request_object, request_data):
    """
    Parameters
    ----------
    request_object
    request_data
    Returns
    -------
    response of put call
    """
    with request_object.put(request_data.endpoint,
                            headers=request_data.headers,
                            data=request_data.body,
                            catch_response=True, verify=False) as response:
        return response


def make_delete_request(request_object, request_data):
    """
    Parameters
    ----------
    request_object
    request_data
    Returns
    -------
    response of delete call
    """
    with request_object.delete(request_data.endpoint,
                               headers=request_data.headers,
                               catch_response=True, verify=False) as response:
        return response
