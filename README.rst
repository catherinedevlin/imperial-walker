===============
Imperial Walker
===============


.. image:: https://img.shields.io/pypi/v/imperial_walker.svg
        :target: https://pypi.python.org/pypi/imperial_walker

.. image:: https://img.shields.io/travis/catherinedevlin/imperial_walker.svg
        :target: https://travis-ci.org/catherinedevlin/imperial_walker

.. image:: https://readthedocs.org/projects/imperial-walker/badge/?version=latest
        :target: https://imperial-walker.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/catherinedevlin/imperial_walker/shield.svg
     :target: https://pyup.io/repos/github/catherinedevlin/imperial_walker/
     :alt: Updates



Walks complex nested data structures to map or do arbitrary commands.


* Free software: MIT license
* Documentation: https://imperial-walker.readthedocs.io.


Usage
-----

The provided `ScoutWalker` returns the [jq](https://stedolan.github.io/jq/) 
paths of all leaf nodes in the data structure.

    >>> from imperial_walker.walker import ScoutWalker 
    >>> data = {'a': 1, 'b': [{'c': 2, 'd': 3}], 'e': {'f': 4}}
    >>> walker = ScoutWalker() 
    >>> list(walker.walk(data))
    ['.a', '.b[].c', '.b[].d', '.e.f']

`ScoutWalker` is one sample subclass of `Walker`.  Write custom 
subclasses for arbitrary behavior.

Features
--------

* TODO

- Hooks for `at_branch`, `at_leaf` (TODO)

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
