from abstracts.singleton import Singleton
from application import Application
import argparse


class Entry(metaclass=Singleton):
    _app = None

    def __init__(self):
        super().__init__()
        self.parser = argparse.ArgumentParser(description='Run Spider')
        self.args = self.build_parser()

    def build_parser(self):
        self.parser.add_argument('--spider_type', dest='spider_type', required=False, help='spider type', default='default')
        self.parser.add_argument('--task_name', dest='task_name', required=False, help='task name', default='default')
        self.parser.add_argument('--debug', dest='debug', required=False, help='debug signal', default=False)
        return self.parser.parse_args()

    def run(self):
        try:
            self._app = Application().run(self.args.spider_type, self.args.task_name)
        except Exception as e:
            # 异常关闭浏览器
            if self._app is not None:
                self._app.get('browser').close()
            print('into exception')
            print(e)


if __name__ == '__main__':
    Entry().run()
