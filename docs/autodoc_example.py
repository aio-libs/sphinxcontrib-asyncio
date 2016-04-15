import asyncio


class MyClass:

    def my_func(self):
        """ Normal function """

    @asyncio.coroutine
    def my_coro(self):
        """ This is my coroutine """


@asyncio.coroutine
def coro(param):
    """ Module level async function """
