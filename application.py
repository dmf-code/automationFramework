from core.manages.component_manager import ComponentManager
from core.manages.global_manager import GlobalManager
from core.manages.hook_manager import HookManager
from core.manages.for_manager import ForManager
from abstracts.singleton import Singleton
from core.browser import Browser
from core.engine import Engine


class Application(metaclass=Singleton):
    _container = {}
    _spider_type = None
    _task_name = None

    def __init__(self, spider_type: str, task_name: str) -> None:
        self._spider_type = spider_type
        self._task_name = task_name
        self._container['browser'] = Browser
        self._container['engine'] = Engine
        self._container['component_manager'] = ComponentManager
        self._container['global_manager'] = GlobalManager
        self._container['hook_manager'] = HookManager
        self._container['for_manager'] = ForManager

    def app(self) -> 'Application':
        print('app')
        return self

    def instance(self, name):
        return self._container[name]()
