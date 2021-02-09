from abstracts.singleton import Singleton


class Container(metaclass=Singleton):
    __instances = {}

    def instances(self):
        return self.__instances

    def set(self, key, value):
        self.__instances[key] = value

    def get(self, key):
        return self.__instances[key]
