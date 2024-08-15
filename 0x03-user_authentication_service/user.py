#!/usr/bin/env python3
"""
User model module using SQLAlchemy.
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    User model for the users table

    Attributes:
        id (int): The primary key of the user
        email (str): The email of the user, must be unique
        hashed_password (str): The hashed password of the user
        session_id (str, optional): The session ID for the user
        reset_token (str, optional): The reset token for password recovery
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)

    def __repr__(self) -> str:
        """String representation of the user instance"""
        return f"<User(id={self.id}, email='{self.email}')>"
