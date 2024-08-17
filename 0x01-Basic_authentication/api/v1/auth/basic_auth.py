#!/usr/bin/env python3
"""
Basic Auth module for implementing Basic Authentication
"""
from .auth import Auth
from models.user import User
import base64
from base64 import b64decode as b64d
from typing import TypeVar


class BasicAuth(Auth):
    """
    BasicAuth class that inherits from Auth
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Function that returns the base64 part of the Auth header
        """
        if authorization_header is not None:
            if type(authorization_header) is str:
                if authorization_header.startswith('Basic '):
                    return authorization_header.strip().split(' ')[1]
        return None

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Function that decodes the base64 part of the Auth header
        """
        if base64_authorization_header is not None:
            if type(base64_authorization_header) is str:
                try:
                    return b64d(base64_authorization_header).decode('ascii')
                except Exception:
                    return None
        return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Function that extracts user credentials from decoded header str
        """
        if decoded_base64_authorization_header is not None:
            if type(decoded_base64_authorization_header) is str:
                if ':' in decoded_base64_authorization_header:
                    user, passwd = decoded_base64_authorization_header.split(':', 1)
                    return user, passwd
        return None, None
