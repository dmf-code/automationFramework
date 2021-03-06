from abstracts.singleton import Singleton
from playwright.sync_api import sync_playwright
from core.config import Config


class Browser(metaclass=Singleton):
    __browser = None
    __launch = None
    __pages = {}
    __current_page = None
    __browser_type = 'chromium'

    def generate_browser(self, engine, browser_type='chromium'):
        with sync_playwright() as p:
            browser = {'chromium': p.chromium, 'firefox': p.firefox, 'webkit': p.webkit}
            self.__browser = browser[browser_type]
            self.__browser_type = browser_type
            self.open_browser()
            self.open_page()
            engine.scheduler()
            self.close()

    def open_browser(self):
        self.__launch = self.__browser.launch(headless=Config().get()['headless'])

    def open_page(self, name='default'):
        self.__pages[name] = self.__launch.new_page()
        self.__current_page = self.__pages[name]

    def select_page(self, name='default'):
        self.__current_page = self.__pages[name]
        return self.__pages[name]

    def get_current_browser(self):
        return self.__browser

    def get_current_launch(self):
        return self.__launch

    def get_current_page(self):
        return self.__current_page

    def close(self):
        self.__launch.close()
