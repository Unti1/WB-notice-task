import aiohttp
import json

async def get_info_for_article(article):
    standart_url = f'https://card.wb.ru/cards/v1/detail?appType=1&curr=rub&dest=-1257786&spp=30&nm={article}'
    async with aiohttp.ClientSession() as session:
        async with session.get(standart_url) as response:
            result = await response.json()
            return result['data']['products']
        