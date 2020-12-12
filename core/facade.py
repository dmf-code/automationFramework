from abstracts.singleton import Singleton
from utils import convert_big_hump
from core.config import Config
import importlib
import os
import re


class Facade(metaclass=Singleton):
    app = None
    core_name = []

    def __init__(self):
        print(self.core_name)

    def init(self, app):
        self.app = app
        self.core_name.extend(self.recursive_dir(Config().get_dir().manages()))
        self.core_name.extend(self.recursive_dir(Config().get_dir().components()))

    def recursive_dir(self, path, prefix="", result=[]):
        path = path.rstrip(os.path.sep) + os.path.sep
        for p in os.listdir(path):
            if os.path.isfile(path + p):
                if prefix is "":
                    result.append(p)
                else:
                    result.append(prefix + p)
            else:
                self.recursive_dir(path + p, prefix + p + ".", result)

        result = list(filter(lambda x: re.match("\\S+.py$", x), result))
        return result

    def build(self, module, args=None):
        if '{}.py'.format(module) not in self.core_name:
            raise Exception('{} is not exist in dir'.format(module))
        if module not in self.__contains:
            load_module = importlib.import_module('titan.components.{}'.format(module))
            ins = module.split('.')[-1]
            self.__contains[module] = getattr(load_module, convert_big_hump(ins))

        if args is None:
            instance = self.__contains[module]()
        else:
            instance = self.__contains[module](args)
        return instance