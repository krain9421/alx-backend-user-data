#!/usr/bin/env python3
"""
Basic Authentication module for implenting Authentication
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """
    Class template for authentication system
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Method that detemines if a path requires authentication
        Returns: False
        """
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != '/':
            path += '/'
                # if path + '/' in excluded_paths:
                    # return False
        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Method that returns the authorization header
        Returns: None
        """
        if request is None or not request.headers.get('Authorization'):
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method that returns the current user
        Returns: None
        """
        return None
