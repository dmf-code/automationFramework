from abstracts.singleton import Singleton
from core.container import Container
from core.browser import Browser
from core.engine import Engine
from core.facade import Facade


class Application(metaclass=Singleton):
    __container = Container()

    def set(self, name, value):
        self.__container.set(name, value)

    def app(self) -> 'Application':
        return self

    def run(self):
        self.set('app', self)
        self.set('browser', Browser())
        self.set('engine', Engine())
        self.set('facade', Facade())
        self.__container.get('browser').generate_browser(self.__container.get('engine'))

