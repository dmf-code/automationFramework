from abstracts.singleton import Singleton
from playwright import sync_playwright
from utils.log import Log


class Browser(metaclass=Singleton):

    _browser = None
    _launch = None
    _pages = {}
    _current_page = None
    _browser_type = 'chromium'

    def generate_browser(self, browser_type='chromium'):
        with sync_playwright() as p:
            browser = {'chromium': p.chromium, 'firefox': p.firefox, 'webkit': p.webkit}
            self._browser = browser[browser_type]
            self._browser_type = browser_type

        Log().info('generate_browser')

    def open_browser(self):
        self._launch = self._browser.launch(headless=False)
        Log().info('open_browser')

    def open_page(self, name='default'):
        self._pages[name] = self._launch.newPage()
        self._current_page = self._pages[name]

        Log().info('open_page')

    def select_page(self, name='default'):
        self._current_page = self._pages[name]
        return self._pages[name]

    def get_current_browser(self):
        return self._browser

    def get_current_launch(self):
        return self._launch

    def get_current_page(self):
        return self._current_page

    def close(self):
        self._launch.close()
