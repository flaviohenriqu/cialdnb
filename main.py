import asyncio
import sys
from pprint import pprint

import httpx

from tasks import make_request_async


async def main():
    urls = [line.strip() for line in sys.stdin]
    async with httpx.AsyncClient() as client:
        pprint(await asyncio.gather(*[make_request_async(client, url) for url in urls]))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
