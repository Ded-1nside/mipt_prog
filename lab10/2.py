from collections import namedtuple
import asyncio
from concurrent.futures import FIRST_COMPLETED
import aiohttp
from asyncio import create_task

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)

async def fetch_ip(service):
    async with aiohttp.ClientSession() as ses:
        async with ses.get(service.url) as resp:
            data = await resp.json()
            return data[service.ip_attr]


async def asynchronous(a_tuple):
    pending = []
    for st in a_tuple:
        task = create_task(fetch_ip(st))
        pending.append(task)
    await asyncio.wait(pending, return_when = asyncio.FIRST_COMPLETED)


asyncio.run(asynchronous(SERVICES))