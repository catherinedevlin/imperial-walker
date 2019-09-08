# -*- coding: utf-8 -*-

"""Main module."""


def _is_dictlike(data):

    return hasattr(data, "items") and hasattr(data, "keys")


def _is_listlike(data):

    return hasattr(data, "__iter__") and not hasattr(data, "swapcase")


class Walker:

    """Base class for walkers.  
    
    Subclass and replace `walk` for specific functions.
    """

    def walk(self, data, upstream=None):
        """Generic walker that yields all leaves.

        :param data: Data tree to walk over 
        :type data: Any 
        :param upstream: Any data that needs to be carried to branches 
                         from upstream (none for base class)
                         defaults to None
        :type upstream: Any, optional
        """

        if _is_dictlike(data):
            for (k, v) in data.items():
                yield from self.walk(v, upstream=upstream)

        elif _is_listlike(data):
            for itm in data:
                yield from self.walk(itm, upstream=upstream)

        else:
            yield data


class ScoutWalker(Walker):
    def walk(self, data, upstream=None):
        """Yields jq paths of all leaves.

        :param data: Data tree to walk over 
        :type data: Any 
        :param upstream: jq path of the structure 
                         to this point; defaults to None
        :type upstream: str 
        """

        if upstream is None:
            upstream = "."

        if _is_dictlike(data):
            for (k, v) in data.items():
                path = "%s.%s" % (upstream, k)
                yield from self.walk(v, upstream=path)

        elif _is_listlike(data):
            for itm in data:
                path = "%s[]" % upstream
                yield from self.walk(itm, upstream=path)

        else:
            path = upstream.replace("..", ".")
            yield path
