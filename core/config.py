from abstracts.singleton import Singleton
from core import ROOT, ENV, dirs
import yaml
import os


class Config(metaclass=Singleton):
    __yaml_config = None
    __dir = dirs

    def __init__(self):
        with open(ROOT + os.path.sep + 'config.yml') as f:
            self.__yaml_config = yaml.load(f.read(), Loader=yaml.FullLoader)[ENV]

    def __getattr__(self, item):
        print(item)

    def get(self):
        return self.__yaml_config

    def get_dir(self):
        return self.__dir


if __name__ == '__main__':
    print(Config().get())
