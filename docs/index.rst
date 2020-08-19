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

1. Install from PyPI:

.. code-block:: shell

   $ pip install sphinxcontrib-asyncio

2. Enable ``sphinxcontrib-asyncio`` extension in your ``conf.py``:

.. code-block:: python

   extensions = ['sphinxcontrib.asyncio']

Usage In Documents
------------------

Use ``cofunction`` instead of ``function``::

   .. cofunction:: coro(a, b)

      Simple coroutine function.

.. cofunction:: coro(a, b)
   :noindex:

   Simple coroutine function.

and ``comethod`` instead of ``method``::

   .. class:: A

      .. comethod:: meth(self, param)

         Coroutine method.

.. class:: A
   :noindex:

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
   :noindex:

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
   :noindex:

   A function can be used in ``async with`` and ``await`` context.

``comethod`` also may be used with **staticmethod** and
**classmethod** optional specifiers, e.g.::

   .. class:: A

      .. comethod:: f(cls, arg)
         :classmethod:

         This is classmethod

.. class:: A
   :noindex:

   .. comethod:: f(cls, arg)
      :classmethod:

      This is classmethod


Usage in `sphinx.ext.autodoc` extension
---------------------------------------

.. currentmodule:: autodoc_example

``sphinxcontrib-asyncio`` add special documenters for autodocs, which will use
*cofunction* and *comethod* directives if the function is an ``async def`` or
is marked with ``coroutine`` decorator.

For example this source:

.. literalinclude:: autodoc_example.py
   :language: python


Using this simple configuration in your `.rst` file::

   .. autocofunction:: coro

   .. autoclass:: MyClass
      :members:

Will yield next documentation:

.. autocofunction:: coro
   :noindex:

.. autoclass:: MyClass
   :members:
   :noindex:

You can set directive options by adding it to `autocofunction` and
`autocomethod` directives::

   .. autocofunction:: coro
      :async-for:
      :coroutine:

.. autocofunction:: coro
   :async-for:
   :coroutine:
   :noindex:

You can also force `coroutine` prefix on not-coroutine method by overriding it
as `autocomethod` directive::

   .. autoclass:: MyClass
      :members:
      :exclude-members: my_func

      .. autocomethod:: my_func()

.. autoclass:: MyClass
   :members:
   :exclude-members: my_func
   :noindex:

   .. autocomethod:: my_func()


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
