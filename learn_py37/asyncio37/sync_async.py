import asyncio
import sys
import time
import urllib.request as request

import aiohttp

URL = 'https://api.github.com/events'
MAX_CLIENTS = 3


def fetch_sync(pid):
    print('Fetch sync process {} started'.format(pid))
    start = time.time()
    response = request.urlopen(URL)
    # proxy_handler = request.ProxyHandler({'http': PROXY_HOST})
    # opener = request.build_opener(proxy_handler)
    # req = opener.open(URL)
    # response = request.urlopen(req)
    datetime = response.getheader('Date')

    print('Process {}: {}, took: {:.2f} seconds'.format(
        pid, datetime, time.time() - start))

    return datetime


async def aiohttp_get(url):
    """Nothing to see here, carry on ..."""
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.get(url) as response:
            return response


async def fetch_async(pid):
    print('Fetch async process {} started'.format(pid))
    start = time.time()
    response = await aiohttp_get(URL)
    datetime = response.headers.get('Date')

    print('Process {}: {}, took: {:.2f} seconds'.format(
        pid, datetime, time.time() - start))

    response.close()
    return datetime


def synchronous():
    start = time.time()
    for i in range(1, MAX_CLIENTS + 1):
        fetch_sync(i)
    print("Process took: {:.2f} seconds".format(time.time() - start))


async def asynchronous():
    start = time.time()
    tasks = [asyncio.create_task(
        fetch_async(i)) for i in range(1, MAX_CLIENTS + 1)]
    await asyncio.wait(tasks)
    print("Process took: {:.2f} seconds".format(time.time() - start))


if __name__ == '__main__':
    print('Synchronous:')
    synchronous()

    print('Asynchronous:')
    if (sys.platform.startswith('win')
            and sys.version_info[0] == 3
            and sys.version_info[1] >= 8):
        policy = asyncio.WindowsSelectorEventLoopPolicy()
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(asynchronous())
