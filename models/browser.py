from playwright.async_api import async_playwright, Page, Browser
from typing import Optional
import asyncio

class Browser:
    """Standart async Browser Model
    """
    def __init__(self) -> None:
        self.playwright = None
        self.browser: Optional[Browser] = None
        self.page: Optional[Page] = None

    async def init_browser(self):
        self.playwright = await async_playwright().start()
        self.browser = self.playwright.chromium.launch()
        self.page = self.browser.new_page()
    
    async def close_browser(self):
        if self.browser:
            await self.browser.close()
    