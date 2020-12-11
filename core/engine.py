from abstracts.singleton import Singleton
from core.browser import Browser
import time


class Engine(metaclass=Singleton):

    def __init__(self):
        pass

    def scheduler(self):
        page = Browser().get_current_page()
        print(page)
        page.goto('https://www.baidu.com')
        time.sleep(10)
