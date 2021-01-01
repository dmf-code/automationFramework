from abstracts.singleton import Singleton


class Browser(metaclass=Singleton):
    _browser = None
    _launch = None
    _contents = {}
    _pages = {}
    _current_page = None
    _browser_type = 'chromium'

    def init(self, browser_type: str, browser: dict):
        self._browser_type = browser_type
        self._browser = browser[browser_type]

    def launch(self):
        self._launch = self._browser.launch(headless=False)

    def open_content(self, name='default'):
        self._contents[name] = {'content': self._launch.newContext()}

    def open_page(self, name='default', page_name='default'):
        self._contents[name][page_name] = self._launch.newPage()
        self._current_page = self._contents[name][page_name]

    def select_page(self, name='default', page_name='default'):
        self._current_page = self._contents[name][page_name]
        return self._current_page

    def get_current_browser(self):
        return self._browser

    def get_current_launch(self):
        return self._launch

    def get_current_content(self):
        return self._contents

    def get_current_page(self):
        return self._current_page

    def close(self):
        return self._launch.close()
