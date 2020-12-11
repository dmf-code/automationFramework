from abstracts.singleton import Singleton
from core.browser import Browser
from core.engine import Engine
import argparse


class Entry(metaclass=Singleton):
    def __init__(self):
        super().__init__()
        self.parser = argparse.ArgumentParser(description='Run Spider')
        self.args = self.build_parser()

    def build_parser(self):
        self.parser.add_argument('--type', dest='spider_type', required=False, help='spider type', default='default')
        self.parser.add_argument('--name', dest='task_name', required=False, help='task name', default='default')
        self.parser.add_argument('--debug', dest='debug', required=False, help='debug signal', default=False)
        return self.parser.parse_args()

    def run(self):
        try:
            Browser().generate_browser()
            Browser().open_browser()
            Browser().open_page()
            Engine().scheduler()
            Browser().close()
        except Exception as e:
            print('into exception')
            print(e)


if __name__ == '__main__':
    Entry().run()
