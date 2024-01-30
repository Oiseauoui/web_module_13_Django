# users/utils.py
from django.db import connection


def get_postgresql():
    return connection.cursor()
