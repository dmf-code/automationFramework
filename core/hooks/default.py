from core.hooks.base import Base
from core.facade import Facade
import json


class Default(Base):
    def before(self, *args, **kwargs):
        pass

    def running(self, *args, **kwargs):
        pass

    def after(self, *args, **kwargs):
        pass

    def exception(self, *args, **kwargs):
        pass

    def terminate(self, *args, **kwargs):
        pass

    def load_params(self, *args, **kwargs):
        pass

    def load_commands(self, *args, **kwargs):
        config = Facade().get('config')
        with open(config.get_dir().commands() + 'default.json', 'r', encoding='utf-8') as f:
            commands = json.load(f)
            return commands

    def data_processing(self, *args, **kwargs):
        data = Facade().get('global').get('html')
        print(data)
