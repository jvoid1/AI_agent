from playwright.async_api import async_playwright
from .base_website import BaseWebsite

class MonparisWebsite(BaseWebsite):
    async def navigate_to_billing(self):
        await self.page.wait_for_timeout(2000)
        facturacion_button = await self.page.query_selector(self.selectors["facturacion_button"])
        await facturacion_button.click()
        print("Clicked on FACTURACION button")
        await self.page.wait_for_timeout(2000)
            
        await self.page.wait_for_url("**/facturacion")
        current_url = self.page.url
        print(f"Current URL: {current_url}")
        await self.page.wait_for_timeout(5000)

        # Buttons on the page
        buttons = self.page.locator("button, a")
        button_count = await buttons.count()
        target_button = buttons.nth(20)
        await target_button.scroll_into_view_if_needed()
        await target_button.click(force=True)
        print("Clicked in CUMBRES button")
        await self.page.wait_for_timeout(5000)
        
        with context.expect_page() as new_page_info:
            new_page = await new_page_info.value
            new_page.wait_for_load_state()
            print(f"New page URL: {new_page.url}")
        
        await target_button.click(force=True)
        print("Successfully clicked on button CUMBRES")
        print(target_button)
        
        await self.page.wait_for_timeout(2000)
        new_url = self.page.url
        print(f"Redirected to: {new_url}")
        await self.page.wait_for_url("https://ww.wansoft.net/Wansoft.Web/Public/ElectronicInvoice40?sid=3774&hasCode=false")
        
        # Wait for form fields to be loaded
        Orden = self.page.locator("//*[@id='IssueInvoice_Step1Div']/div[2]/div[2]").wait_for(state="attached", timeout=10000)
        if not Orden:
            print("Error: Form fields not loaded in time")
        else:
            print("Form fields loaded successfully")

        # Map selectors to form data
        fields = {
            "OrderNumber": "#OrderNumber",
            "Total": "#Total",
            "TotalInvoice": "#TotalInvoice",
            "rfc": "#rfc",
            "legalName": "#legalName",
            "email": "#email",
            "CP": "#CP"
        }

        # Fill each field
        for field_name, selector in fields.items():
            try:
                # Wait for field to be visible
                field = await self.page.wait_for_selector(selector, timeout=5000)
                if field:
                    value = form_data.get(field_name, "")
                    print(f"Filling {field_name} with value {value}")
                    
                    # Handle select elements differently
                    if "select" in selector:
                        await field.select_option(value=value)
                    else:
                        await field.fill(value)
                    
                    await self.page.wait_for_timeout(500)
                else:
                    print(f"Field not found: {field_name}")
            except Exception as e:
                print(f"Error filling field {field_name}: {str(e)}")
                # Take screenshot for debugging
                await self.page.screenshot(path=f"error_{field_name}.png")

        print("Form filled successfully")
                    
        await self.page.wait_for_timeout(3000)


    async def fill_form(self, form_data: dict):
        await self.page.wait_for_timeout(5000)
        iframe = self.page.frame_locator(self.selectors["iframe"])
        await self.page.wait_for_timeout(5000)
        
        # Fill store selector
        store_selector = iframe.locator(self.selectors["store_selector"])
        await store_selector.select_option(value=form_data["store_value"])
        
        # Fill ticket number
        ticket_input = iframe.locator(self.selectors["ticket_input"])
        await ticket_input.fill(form_data["ticket_number"])
        
        # Fill total amount
        total_input = iframe.locator(self.selectors["total_input"])
        await total_input.fill(form_data["total_amount"])

    async def submit_form(self):
        iframe = self.page.frame_locator(self.selectors["iframe"])
        submit_button = iframe.locator(self.selectors["submit_button"])
        await submit_button.click()