from .base_website import BaseWebsite

class AlseaWebsite(BaseWebsite):
    async def navigate_to_billing(self):
        await self.page.wait_for_timeout(5000)
        await self.page.screenshot(path="alsea_home.png")
        await self.page.wait_for_timeout(5000)


    async def fill_form(self, form_data: dict):
        await self.page.wait_for_timeout(5000)
        
        await self.page.wait_for_timeout(5000)

    async def submit_form(self):
        iframe = self.page.frame_locator(self.selectors["iframe"])
        submit_button = iframe.locator(self.selectors["submit_button"])
        await submit_button.click()