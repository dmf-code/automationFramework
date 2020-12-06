from abstracts.singleton import Singleton


class Container(metaclass=Singleton):
    _instances = {}

    def instances(self):
        return self._instances

    def set(self, key, value):
        self._instances[key] = value

    def get(self, key):
        return self._instances[key]
