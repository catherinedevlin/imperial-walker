# -*- coding: utf-8 -*-

"""Main module."""


def _is_dictlike(data):

    return hasattr(data, "items") and hasattr(data, "keys")


def _is_listlike(data):

    return isinstance(data, list)


class Walker:

    pass


class ScoutWalker(Walker):
    def __init__(self):
        pass

    def walk(self, data, path=None):

        # make path more generic

        # call path initialization hook
        if path is None:
            path = ["."]

        if _is_dictlike(data):
            for (k, v) in data.items():
                # call branch hook
                # generic passer-on of upstream info (more generic than path)
                yield from self.walk(v, path=(path + [f".{k}"]))

        elif _is_listlike(data):
            for itm in data:
                # call branch hook
                # generic passer-on of upstream info (more generic than path)
                yield from self.walk(itm, path=(path + ["[]"]))

        else:
            # call Finalizer hook
            # call leaf hook
            yield "".join(path).replace("..", ".")
