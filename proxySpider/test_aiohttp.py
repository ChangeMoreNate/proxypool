import aiohttp
import asyncio






async def getpage():
    pass



async def request():
    pass



tasks = [asyncio.ensure_future(request()) for _ in range(10)]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))



