# -*- coding: utf-8 -*-
from core.manages.global_manager import GlobalManager
from functools import wraps
import timeit


def run_time_sum(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = timeit.default_timer()
        __func = func(*args, **kwargs)
        end = timeit.default_timer()
        if GlobalManager().debug:
            print('run time: {} s'.format(str(round(end - start, 4))))
        return __func

    return wrapper
