#!/usr/bin/python3
"""
Basic Authentication module
"""
import flask
from flask import rerquest


class Auth():
    """
    Template for authentication system
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns: False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Returns: None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns: None
        """
        return None
