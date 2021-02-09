# -*- coding: utf-8 -*-
from core.components import Base


class Wait(Base):

    def have_element(self):
        WebDriverWait(self.driver, self.params.get('time', 10)).until(
            EC.presence_of_element_located(By.XPATH, self.params['xpath'])
        )

