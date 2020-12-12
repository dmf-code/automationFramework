# -*- coding: utf-8 -*-
from core.manages.global_manager import GlobalManager
from utils import make_requests
from core.components import Base
from core.config import Config
import os


class Request(Base):
    def url_format(self):
        if self.params.get('url', None):
            global_type = self.params.get('global_type', None)
            if GlobalManager().debug:
                print('global_type：', global_type)
            if global_type is None:
                params = GlobalManager().get()
            else:
                params = GlobalManager().get(type_=global_type)
            url = self.params['url'].format(**params)
            return url

    def get_method(self):
        return self.params.get('method', 'POST')

    def browser(self):
        url = self.url_format()
        if self.params.get('read_cookie', None):
            self.read_cookie()
        self.driver.get(url)
        return self.sleep()

    def default(self):
        url = self.url_format()
        data = self.params.get('data', [])
        make_requests(self.get_method(), url, data=data)

    def read_cookie(self):
        path = Config().get_dir().cookies() + self.params['cookie_name'] + '.txt'
        if not os.path.exists(path):
            raise Exception('cookies not exists')

        with open(path) as f:
            cookies = f.read()
        for cookie in cookies:
            self.driver.add_cookie(cookie)
