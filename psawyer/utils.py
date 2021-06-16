import inspect


def get_kwargs():
    frame = inspect.currentframe().f_back
    keys, _, _, values = inspect.getargvalues(frame)
    kwargs = {}
    for key in keys:
        if key != "self" and values[key] is not None and values[key] != ():
            kwargs[key] = values[key]
    return kwargs
