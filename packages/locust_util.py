"""
    Common util methods that are required in tests.
"""

import random
import string


def unique_name(size=6, chars=string.ascii_uppercase + string.ascii_lowercase):
    """
    Method to generate a unique name for tests
    Parameters
    ----------
    size
    chars

    Returns
    -------
    String of <size> length using uppercase and lowercase letters randomly
    """
    return ''.join(random.choice(chars) for _ in range(size))
