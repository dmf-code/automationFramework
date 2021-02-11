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
        self.parser.add_argument('--spider_type', dest='spider_type', required=False, help='spider type',
                                 default='default')
        self.parser.add_argument('--task_name', dest='task_name', required=False, help='task name', default='default')
        self.parser.add_argument('--params', dest='params', required=False, help='params', default=None)
        return self.parser.parse_args()

    def run(self):
        try:
            self._app = Application().init(self.args.spider_type, self.args.task_name)
            self.parser_params()
            Application().get('browser').generate_browser(Application().get('engine'))
        except Exception as e:
            # 异常关闭浏览器
            if self._app is not None:
                self._app.get('browser').close()
            print('into exception')
            print(e)

    def parser_params(self):
        params = self.args.params
        global_manage = self._app.get('global')
        if params is not None and params is not "":
            items = params.split(";")
            for item in items:
                arr = item.split("=")
                global_manage.set(arr[0], arr[1])


if __name__ == '__main__':
    Entry().run()
