from abstracts.singleton import Singleton
from core.browser import Browser
from core.engine import Engine


class Application(metaclass=Singleton):
    __container = {}

    def __init__(self, browser, engine):
        self.__container['browser'] = browser
        self.__container['engine'] = engine

    def app(self) -> 'Application':
        print('app')
        return self

    # def __get__(self, instance, owner):
    #     print('__get__')
    #     print(instance)
    #     print(owner)
    #     return self.__container.get(instance, None)
    #
    # def __set__(self, instance, value):
    #     print('__set__')
    #     print(instance)
    #     print(value)

    def run(self):
        print('application run')
        self.__container.get('browser').generate_browser(self.__container.get('engine'))

