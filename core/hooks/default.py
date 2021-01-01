# -*- coding: utf-8 -*-
from core.manages.global_manager import GlobalManager
from utils.log import Log
from core.hooks.base import Base
import traceback
from utils import make_requests
import json
import os
from core.config import Config


class Default(Base):

    def before(self, *args, **kwargs):
        pass

    def running(self, *args, **kwargs):
        pass

    def handle(self, *args, **kwargs):
        pass

    def after(self, *args, **kwargs):
        GlobalManager().get_driver().close()
        GlobalManager().get_driver().quit()

    def exception(self, *args, **kwargs):

        msg = 'exception: {} {}'.format(GlobalManager().get('commands.uuid'), traceback.format_exc())
        if GlobalManager().debug:
            print(msg)
        else:
            Log.info(msg)

    def terminate(self, *args, **kwargs):
        pass

    def get_args(self):
        return None

    def load_commands(self, *args, **kwargs):

        if Config().get()['load_command_from_file']:
            with open(Config().get_dir()['configs'] + 'common.json', 'r', encoding='utf-8') as f:
                commands = json.load(f)
        else:
            res = make_requests('GET', 'http://localhost:5000/api/search/common/boss')
            commands = res['data']['jsonText']

        if isinstance(commands, str):
            commands = json.loads(commands)

        return commands
