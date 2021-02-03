# -*- coding: utf-8 -*-
import os

ENV = os.environ.get('ENV', 'development')

# creative dir
CORE = os.path.dirname(os.path.realpath(__file__))

ROOT = os.path.dirname(CORE)

BIN_DIR = ROOT + os.path.sep + 'bin' + os.path.sep

LOGS_DIR = ROOT + os.path.sep + 'logs' + os.path.sep

MANAGES_DIR = CORE + os.path.sep + 'manages' + os.path.sep

COMPONENTS_DIR = CORE + os.path.sep + 'components' + os.path.sep

HOOKS_DIR = CORE + os.path.sep + 'hooks' + os.path.sep

COMMANDS_DIR = CORE + os.path.sep + 'commands' + os.path.sep

CONFIGS_DIR = ROOT + os.path.sep + 'configs' + os.path.sep

STORAGE_DIR = ROOT + os.path.sep + 'storages' + os.path.sep

COOKIES_DIR = STORAGE_DIR + os.path.sep + 'cookies' + os.path.sep

