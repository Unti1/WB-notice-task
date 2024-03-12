import aiohttp
import json

async def get_info_for_article(request):
    async with aiohttp.ClientSession() as session:
        async with session.get(request) as response:
            return await response.json()

