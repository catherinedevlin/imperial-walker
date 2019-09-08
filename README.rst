===============
Imperial Walker
===============


.. image:: https://img.shields.io/pypi/v/imperial_walker.svg
        :target: https://pypi.python.org/pypi/imperial_walker

.. image:: https://img.shields.io/travis/catherinedevlin/imperial-walker.svg
        :target: https://travis-ci.org/catherinedevlin/imperial-walker

.. image:: https://readthedocs.org/projects/imperial-walker/badge/?version=latest
        :target: https://imperial-walker.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/catherinedevlin/imperial-walker/shield.svg
     :target: https://pyup.io/repos/github/catherinedevlin/imperial-walker/
     :alt: Updates



Walks complex nested data structures to map or do arbitrary commands.


* Free software: MIT license
* Documentation: https://imperial-walker.readthedocs.io.


Usage
-----

The base class ``Walker`` simply yields the value of each leaf.

    >>> data = {"a": 1, "b": ({"c": 2, "d": 3}), "e": {"f": 4}}
    >>> walker = Walker()
    >>> list(walker.walk(data))
    [1, 2, 3, 4]

The provided ``ScoutWalker`` returns the jq_ 
paths of all leaf nodes in the data structure.

    >>> from imperial_walker.walker import ScoutWalker 
    >>> data = {'a': 1, 'b': [{'c': 2, 'd': 3}], 'e': {'f': 4}}
    >>> walker = ScoutWalker() 
    >>> list(walker.walk(data))
    ['.a', '.b[].c', '.b[].d', '.e.f']

``ScoutWalker`` is one sample subclass of ``Walker``.  Write custom 
subclasses, overriding ``Walker.walk`` and imitating its structure,
for arbitrary behavior.

When mapping large data trees, it may be useful to postprocess 
``ScoutWalker``'s output with ``set`` or ``collections.Counter``.

Notes
-----

``Walker.walk`` is simple enough that writing it to invoke hooks seemed 
to create more confusion than it solved; rather, just copy-and-paste 
``walk`` from ``Walker`` or ``ScoutWalker`` to your subclass and modify 
as needed.

So far, no class data is used, so perhaps the whole module should be 
rewritten into a set of functions.


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _jq: https://stedolan.github.io/jq/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
