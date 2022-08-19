# -*- coding: utf-8 -*-
"""

UserService class - This class holds the method related to User manipulations.

"""

from server.main.models.user import User
from server.main.services import SQLAlchemyService


class UserService(SQLAlchemyService):
    __model__ = User

    def __init__(self):
        self.parentClassRef = super(UserService, self)

