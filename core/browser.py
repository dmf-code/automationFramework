from abstracts.singleton import Singleton
from playwright import async_playwright


class Browser(metaclass=Singleton):

    _browser = None
    _launch = None
    _pages = {}
    _current_page = None
    _browser_type = 'chromium'

    def generate_browser(self, browser_type='chromium'):
        with async_playwright() as p:
            browser = {'chromium': p.chromium, 'firefox': p.firefox, 'webkit': p.webkit}
            self._browser = browser[browser_type]
            self._browser_type = browser_type

    def open_browser(self):
        self._launch = self._browser.launch(headless=False)

    def open_page(self, name='default'):
        self._pages[name] = self._launch.newPage()
        self._current_page = self._pages[name]

    def select_page(self, name='default'):
        self._current_page = self._pages[name]
        return self._pages[name]

    def close(self):
        self._launch.close()
