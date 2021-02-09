# -*- coding: utf-8 -*-
from core.components import Base
from core.config import Config
import json
import os


class Cookie(Base):
    def write_file(self):
        cookie = self.driver.get_cookies()
        path = Config().get_dir().cookies() + self.params['cookie_name'] + '.txt'
        with open(path, 'w') as f:
            json.dump(cookie, f)

        return path
