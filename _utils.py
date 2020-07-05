import os
from typing import Optional


def get_env(varname: str, default: str = None) -> Optional[str]:
    """
    This method returns default value of an environment variable when provided environment variable exists but empty.
    :param varname: name of the environment variable
    :param default: default value to be returned if varname does not exist as env var or exists as env var and empty
    :return: str
    """
    value = os.getenv(varname)
    if value is None or value == '':
        return default
    return value
