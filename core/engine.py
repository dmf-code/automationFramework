from abstracts.singleton import Singleton
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
        time.sleep(1)
