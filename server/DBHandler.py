"""
Export an object that will be singleton and will be used for the communication with the DB.
"""

from tinydb import TinyDB

from singleton import singleton


@singleton
class DBHandler(TinyDB):
    pass
