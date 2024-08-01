#!/usr/bin/env python3
"""Module for defining filter logger function"""
import re
from typing import List


def filter_datum(fld: List[str], rdct: str, msg: str, sep: str) -> str:
    """
    returns the log message obfuscated:

    Arguments:
    fld: a list of strings representing all fields to obfuscate
    rdct: a string representing by what the field will be obfuscated
    msg: a string representing the log line
    sep: a string representing by which character is separating
        all fields in the log line
    """
    for f in fld:
        pattern = '{}=[^;]+\\{}'.format(f, sep)
        msg = re.sub(pattern, '{}={}{}'.format(f, rdct, sep), msg)
    return msg
