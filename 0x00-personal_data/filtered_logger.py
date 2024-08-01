#!/usr/bin/env python3
"""Module for defining filter logger function"""
import re
from typing import List


def filter_datum(fld: List[str], rdct: str, msg: str, sep: str) -> str:
    """Returns the log message obfuscated:"""
    for f in fld:
        msg = re.sub(f'{f}=[^;]+\\{sep}', f'{f}={rdct}{sep}', msg)
    return msg
