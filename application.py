from abstracts.singleton import Singleton
from core.container import Container


class Application(metaclass=Singleton):
    __container = Container()

    def set(self, name, value):
        self.__container.set(name, value)

    def app(self) -> 'Application':
        print('app')
        return self

    def run(self):
        self.__container.get('browser').generate_browser(self.__container.get('engine'))

