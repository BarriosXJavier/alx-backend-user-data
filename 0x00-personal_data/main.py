#!/usr/bin/env python3
"""
Main py file
"""


hash_password = __import__('encrypt_password').hash_password

password = "MyAmazingPassw0rd"
print(hash_password(password))
