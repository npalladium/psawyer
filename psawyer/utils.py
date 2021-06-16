import inspect
from enum import Enum


def get_kwargs():
    frame = inspect.currentframe().f_back
    keys, _, _, values = inspect.getargvalues(frame)
    kwargs = {}
    for key in keys:
        if key != "self" and values[key] is not None and values[key] != ():
            kwargs[key] = values[key]
    if kwargs.get("fields") is not None and "created_utc" not in kwargs.get("fields"):
        kwargs["fields"] = kwargs["fields"] + ("created_utc",)
    return kwargs


class SortOption(str, Enum):
    asc = "asc"
    desc = "desc"
