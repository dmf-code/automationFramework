from abstracts.singleton import Singleton
from core.facade import Facade
from .browser import Browser
import time


class Engine(metaclass=Singleton):

    def __init__(self):
        print('engine init')
        pass

    def scheduler(self):
        print('into scheduler')
        page = Browser().get_current_page()
        print('page')
        print(page)
        page.goto('https://www.baidu.com')
        print(Facade().core_name)
        time.sleep(1)
