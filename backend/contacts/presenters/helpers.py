from django.core.cache import cache
from typing import Any
import math


def round_floor_number(number: Any) -> int:
    return math.floor(number)


def clear_cache(function):
    def wrap(request, *args, **kwargs):
        cache.clear()
        return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap