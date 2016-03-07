.. sphinxcontrib-asyncio documentation master file, created by
   sphinx-quickstart on Fri Mar  4 23:56:21 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. default-domain:: py

sphinxcontrib-asyncio
=====================

Add :ref:`coroutine<coroutine>` markup support to sphinx-based docs.

.. _GitHub: https://github.com/aio-libs/sphinxcontrib-asyncio

Installation
------------

1. Install from PyPI::

   $ pip install sphinxcontrib-asyncio

2. Enable ``sphinxcontrib-asyncio`` extension in your ``conf.py``::

   extensions = ['sphinxcontrib.asyncio']

Usage In Documents
------------------

Use ``cofunction`` instead of ``function``::

   .. cofunction:: coro(a, b)

      Simple coroutine function.

.. cofunction:: coro(a, b)

   Simple coroutine function.

and ``comethod`` instead of ``method``::

   .. class:: A

      .. comethod:: meth(self, param)

         Coroutine method.

.. class:: A

   .. comethod:: meth(self, param)

      Coroutine method.

For more complex markup use *directive options*, e.g.
``async-with`` for *asynchronous context managers factories*::

   .. cofunction:: open_url(param)
      :async-with:

      A function that returns asynchronous context manager.


.. cofunction:: open_url(param)
   :async-with:

   A function that returns asynchronous context manager.

   That means ``open_url`` can be used as::

      async with open_url(arg) as cm:
          pass

``async-for`` may be used for *asynchronous generator* markup::

   .. cofunction:: iter_vals(arg)
      :async-for:

      A function the returns asynchronous generator.

.. cofunction:: iter_vals(arg)
   :async-for:

   A function the returns asynchronous generator.

   ``iter_vals()`` can be used as::

      async for item in iter_args(arg):
          pass

By default ``async-for`` and ``async-with`` suppresses ``coroutine``.

If both ``await func()`` and ``async with func():`` are allowed (func
is both *coroutine* and *asynchronous context manager*) explicit
**coroutine** flag::

   .. cofunction:: get(url)
      :async-with:
      :coroutine:

      A function can be used in ``async with`` and ``await`` context.

.. cofunction:: get(url)
   :async-with:
   :coroutine:

   A function can be used in ``async with`` and ``await`` context.

``comethod`` also may be used with **staticmethod** and
**classmethod** optional specifiers, e.g.::

   .. class:: A

      .. comethod:: f(cls, arg)
         :classmethod:

         This is classmethod

.. class:: A

   .. comethod:: f(cls, arg)
      :classmethod:

      This is classmethod

Discussion list
---------------

*aio-libs* google group: https://groups.google.com/forum/#!forum/aio-libs

Please post your questions and ideas here.

Authors and License
-------------------

The ``sphinxcontrib-asyncio`` package is written by Andrew Svetlov.

It's *Apache 2* licensed and freely available.

Feel free to improve this package and send a pull request to GitHub_.



.. toctree::
   :maxdepth: 2
