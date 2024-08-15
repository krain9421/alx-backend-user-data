#!/usr/bin/env python3
"""
Basic Auth module for implementing Basic Authentication
"""
from .auth import Auth
from models.user import User
import base64
from typing import TypeVar

class BasicAuth(Auth):
    """
    BasicAuth class that inherits from Auth
    """

