from core.manages.component_manager import ComponentManager
from core.manages.global_manager import GlobalManager
from core.manages.hook_manager import HookManager
from core.manages.for_manager import ForManager
from abstracts.singleton import Singleton
from core.container import Container
from core.browser import Browser
from core.engine import Engine
from core.facade import Facade
from core.config import Config


class Application(metaclass=Singleton):
    __spider_type = None
    __task_name = None
    __container = Container()

    def set(self, name, value):
        self.__container.set(name, value)

    def get(self, name):
        self.__container.get(name)

    def app(self) -> 'Application':
        return self

    def container(self):
        return self.__container

    def run(self, spider_type, task_name):
        self.__spider_type = spider_type
        self.__task_name = task_name
        self.set('app', self)
        self.set('browser', Browser())
        self.set('facade', Facade())
        Facade().init(self)

        self.set('component', ComponentManager())
        self.set('for', ForManager())
        self.set('global', GlobalManager())
        self.set('hook', HookManager())
        self.set('config', Config())

        self.set('engine', Engine())
        Engine().init(spider_type)

        self.__container.get('browser').generate_browser(self.__container.get('engine'))

