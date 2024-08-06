#!/usr/bin/env python3
"""
Basic Authentication module for implenting Authentication
"""
from typing import List, TypeVar
from flask import rerquest


class Auth:
    """
    Class template for authentication system
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Method that detemines if a path requires authentication
        Returns: False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Method that returns the authorization header
        Returns: None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method that returns the current user
        Returns: None
        """
        return None
