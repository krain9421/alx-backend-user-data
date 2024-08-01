#!/usr/bin/env python3
"""Module for defining filter logger function"""
import re
from typing import List


def filter_datum(fld: List[str], rdct: str, msg: str, sep: str) -> str:
    """Returns the log message obfuscated:"""
    pattern = '|'.join([f'{field}=[^{sep}]+' for field in fld])
    return re.sub(pattern, lambda m: f'{m.group(0).split("=")[0]}={rdct}', msg)
