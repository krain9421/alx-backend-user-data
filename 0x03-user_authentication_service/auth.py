#!/usr/bin/env python3
"""
User Authentication module
"""
import bcrypt
from typing import TypeVar
import uuid
from db import DB, NoResultFound
from user import User

salted = bcrypt.gensalt()


def _hash_password(password: str) -> bytes:
    """
    Function that returns a hashed password in bytes
    """
    return bcrypt.hashpw(password.encode(), salted)


def _generate_uuid() -> str:
    """
    Function that returns a newly
    generated uuid (uuid4) string
    """
    return str(uuid.uuid4())


class Auth:
    """
    Auth class to implement authentication
    """

    def __init__(self):
        """
        Initializing the Auth Object
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Function that returns a user created
        with the argument values
        """
        if email is None or password is None:
            return None
        if type(email) is not str or type(password) is not str:
            return None
        try:
            new_user = self._db.find_user_by(email=email)
        except NoResultFound:
            new_user = self._db.add_user(email, _hash_password(password))
            return new_user
        raise ValueError("User {} already exists".format(email))

    def valid_login(self, email: str, password: str):
        """
        Function that validates login details
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode(), user.hashed_password)
        except Exception:
            return False

    def create_session(self, email: str):
        """
        Function that creates a user session
        """
        try:
            new_user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(new_user.id, session_id=session_id)
            return session_id
        except Exception:
            return None

    def get_user_from_session_id(self, session_id: str):
        """
        Function that gets a user from a session id
        """
        try:
            new_user = self._db.find_user_by(session_id=session_id)
            return new_user
        except Exception:
            return None

    def destroy_session(self, user_id: str):
        """
        Function that destroys a session
        """
        try:
            new_user = self._db.find_user_by(id=user_id)
            self._db.update_user(new_user.id, session_id=None)
        finally:
            return None

    def get_reset_password_token(self, email: str):
        """
        Function that resets a token
        """
        try:
            new_user = self._db.find_user_by(email=email)
            reset_token = _generate_uuid()
            self._db.update_user(new_user.id, reset_token=reset_token)
            return reset_token
        except Exception:
            raise ValueError

    def update_password(self, reset_token: str, password: str):
        """
        Function that updates a user password
        """
        try:
            new_user = self._db.find_user_by(reset_token=reset_token)
            self._db.update_user(new_user.id,
                                 hashed_password=_hash_password(password))
            self._db.update_user(new_user.id, reset_token=None)
        except Exception:
            raise ValueError
