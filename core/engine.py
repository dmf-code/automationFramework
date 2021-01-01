from core.manages.component_manager import ComponentManager
from core.manages.global_manager import GlobalManager
from core.manages.hook_manager import HookManager
from abstracts.singleton import Singleton
from playwright import sync_playwright
from utils.printer import Printer
from .browser import Browser
from utils.log import Log
import time
import re


class Engine(metaclass=Singleton):
    _commands = None

    def __init__(self):
        print('engine init')
        pass

    def run(self, browser_type='chromium'):
        try:
            print('into engine run')
            with sync_playwright() as p:
                browser = {'chromium': p.chromium, 'firefox': p.firefox, 'webkit': p.webkit}
                Browser().init(browser_type, browser)
                Browser().launch()
                Browser().open_content()
                Browser().open_page()
                self.scheduler()
                Browser().close()
        except Exception as e:
            Browser().close()
            print('into engine run except')
            print(e)

    def scheduler(self):
        try:
            print('into engine scheduler')
            if self._commands is None:
                raise Exception('Engine scheduler: commands is None')

            self.execute(self._commands, 0)
        except Exception as e:
            Log().info(e)

    def execute(self, commands, depth):
        GlobalManager().if_turn_on()
        GlobalManager().depth = depth
        for command in commands:

            if isinstance(command, list):
                self.execute(command, depth + 1)
                GlobalManager().if_turn_on()

                while GlobalManager().is_loop:
                    self.execute(command, depth + 1)
                    GlobalManager().if_turn_on()

                GlobalManager().depth = depth
                continue

            component_name = command['component'].lower()
            component_args = command.get('args', {})
            component_type = command.get('type', 'default')

            if GlobalManager().debug:
                Printer().init()
                Printer().add_row(['exec command', command])
                Printer().add_row(['before_if_status', GlobalManager().is_if])
                Printer().add_row(['before_break_status', GlobalManager().is_break])
                Printer().add_row(['before_loop_status', GlobalManager().is_loop])
                Printer().output()

            if command.get('db_args', None):
                component_args['db_args'] = GlobalManager().get(component_args['dbArgs'], '_db_args')

            GlobalManager().component_name = component_name
            GlobalManager().component_type = component_type

            component = ComponentManager().build(component_name, component_args)

            result = self.filter(component_args, component.run(component_type))

            if command.get('return', None):
                GlobalManager().set(command['return'], result)

            if GlobalManager().debug:
                Printer().init()
                Printer().add_row(['after_if_status ', GlobalManager().is_if])
                Printer().add_row(['after_break_status ', GlobalManager().is_break])
                Printer().add_row(['after_loop_status ', GlobalManager().is_loop])
                Printer().output()

            if component_name == 'if' and not GlobalManager().is_if:
                return

            if GlobalManager().is_break:
                return

            if not GlobalManager().is_loop:
                return

    @staticmethod
    def filter(component_args, text):
        if component_args.get('filter', None) is None:
            return text

        pattern = component_args.get('pattern', None)
        if pattern:
            index = component_args.get('index', None)
            text = re.match(pattern, text).group(index if index else 0)

        return text
