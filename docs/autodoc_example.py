import asyncio


class MyClass:

    def my_func(self):
        """ Normal function """

    @asyncio.coroutine
    def my_coro(self):
        """ This is my coroutine """

    async def my_async_func(self):
        """ This is my async function """
