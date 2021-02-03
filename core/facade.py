from abstracts.singleton import Singleton
from utils import convert_big_hump
from core.config import Config
import importlib
import os
import re


class Facade(metaclass=Singleton):
    app = None

    def init(self, app):
        self.app = app

    def get(self, name):
        return self.app.container().get(name)
