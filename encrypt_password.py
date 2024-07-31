#!/usr/bin/env python3
"""
Encrypting the user passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    returns a salted, hashed password
    """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    takes two arguments and returns a boolean
    """
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        valid = True
    return valid
