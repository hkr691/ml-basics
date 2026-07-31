from enum import Enum

class Movie:
    def __init__(self, id, title):
        self._id = id
        self._title = title
    
    @property
    def id(self):
        return self._id
    
    @property
    def title(self):
        return self._title

class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
    
    @property
    def user_id(self):
        return self._user_id

