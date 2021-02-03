from abstracts.singleton import Singleton
from core import ROOT, BIN_DIR, \
    STORAGE_DIR, LOGS_DIR, \
    MANAGES_DIR, COMPONENTS_DIR, \
    CONFIGS_DIR, HOOKS_DIR, \
    COMMANDS_DIR, COOKIES_DIR


class Dir(metaclass=Singleton):
    def __init__(self):
        self.path = {
            'root': ROOT,
            'bin': BIN_DIR,
            'storage': STORAGE_DIR,
            'logs': LOGS_DIR,
            'manages': MANAGES_DIR,
            'components': COMPONENTS_DIR,
            'configs': CONFIGS_DIR,
            'hooks': HOOKS_DIR,
            'commands': COMMANDS_DIR,
            'cookies': COOKIES_DIR
        }

    def root(self):
        return self.path['root']

    def bin(self):
        return self.path['bin']

    def storage(self):
        return self.path['storage']

    def logs(self):
        return self.path['logs']

    def manages(self):
        return self.path['manages']

    def components(self):
        return self.path['components']

    def configs(self):
        return self.path['configs']

    def hooks(self):
        return self.path['hooks']

    def commands(self):
        return self.path['commands']

    def cookies(self):
        return self.path['cookies']
