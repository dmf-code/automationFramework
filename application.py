from abstracts.singleton import Singleton
from core.browser import Browser
from core.engine import Engine


class Application(metaclass=Singleton):
    __container = {}

    def set(self, name, value):
        self.__container[name] = value

    def app(self) -> 'Application':
        print('app')
        return self

    def run(self):
        print('application run')
        self.__container.get('browser').generate_browser(self.__container.get('engine'))

