# -*- coding: utf-8 -*-
from core.components import Base
import time


class Click(Base):
    def default(self):
        self.driver.find_element_by_xpath(self.params['xpath']).click()
        self.sleep()
