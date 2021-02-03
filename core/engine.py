from abstracts.singleton import Singleton
from utils.printer import Printer
from core.facade import Facade
import traceback
import re


class Engine(metaclass=Singleton):

    __hook = None
    __param = None
    __command = None

    def __init__(self):
        print('engine init')
        pass

    def init(self, spider_type):
        print('into init engine')
        hook = Facade().get('hook').build(spider_type)

        self.__hook = hook
        self.__param = hook.load_params()
        self.__command = hook.load_commands()
        if Facade().get('global').debug:
            print(self.__hook)
            print(self.__command)

    def scheduler(self):
        print('into scheduler')
        try:
            self.__hook.before()
            self.execute(self.__command, 0)
            self.__hook.after()
            self.__hook.data_processing()
        except Exception as e:
            print(e)
            print(traceback.print_exc())
            print("into engine exception")
            self.__hook.exception()
        finally:
            self.__hook.terminate()

    def execute(self, commands, depth):
        self.__hook.running()
        global_manage = Facade().get('global')
        component_manage = Facade().get('component')

        global_manage.if_turn_on()
        global_manage.depth = depth
        for command in commands:
            if isinstance(command, list):
                self.execute(command, depth + 1)
                global_manage.if_turn_on()

                while global_manage.is_loop:
                    self.execute(command, depth + 1)
                    global_manage.if_turn_on()

                global_manage.depth = depth
                continue

            component_name = command['component'].lower()
            component_args = command.get('args', {})
            component_type = command.get('type', 'default')

            if global_manage.debug:
                Printer().init()
                Printer().add_row(['exec command', command])
                Printer().add_row(['before_if_status', global_manage.is_if])
                Printer().add_row(['before_break_status', global_manage.is_break])
                Printer().add_row(['before_loop_status', global_manage.is_loop])
                Printer().output()

            if command.get('db_args', None):
                component_args['db_args'] = global_manage.get(component_args['dbArgs'], '_db_args')

            global_manage.component_name = component_name
            global_manage.component_type = component_type

            component = component_manage.build(component_name, component_args)

            result = self.result_filter(component_args, component.run(component_type))

            if command.get('return', None):
                global_manage.set(command['return'], result)

            if global_manage.debug:
                Printer().init()
                Printer().add_row(['after_if_status ', global_manage.is_if])
                Printer().add_row(['after_break_status ', global_manage.is_break])
                Printer().add_row(['after_loop_status ', global_manage.is_loop])
                Printer().output()

            if component_name == 'if' and not global_manage.is_if:
                return

            if global_manage.is_break:
                return

            if not global_manage.is_loop:
                return

    @staticmethod
    def result_filter(component_args, text):
        if component_args.get('filter', None) is None:
            return text

        pattern = component_args.get('pattern', None)
        if pattern:
            index = component_args.get('index', None)
            text = re.match(pattern, text).group(index if index else 0)

        return text