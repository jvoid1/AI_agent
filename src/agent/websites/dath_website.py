from .base_website import BaseWebsite

class DathWebsite(BaseWebsite):
    async def navigate_to_billing(self):
        facturacion_button = await self.page.query_selector(self.selectors["facturacion_button"])
        if facturacion_button:
            await facturacion_button.click()
            await self.page.wait_for_timeout(2000)
            await self.page.mouse.click(10, 10)
            await self.page.wait_for_timeout(5000)
            
            print("Waiting for iframe to load...")
            iframe = self.page.frame_locator(self.selectors["iframe"])
            await self.page.wait_for_timeout(5000)
            
            # Iframe context
            try:
                print("Searching for 'Facturar' button in iframe...")
                facturar_button = iframe.locator('button:has-text("Facturar")')
                
                await facturar_button.wait_for(state="visible", timeout=10000)
                print(f"Found Facturar button")
                    
                # Click in Facturar button
                await facturar_button.click()
                print("Successfully clicked on 'Facturar' button")
                await self.page.wait_for_timeout(2000)

                # Fill the form fields
                iframe = self.page.frame_locator('iframe[src="https://dath.intelisiscloud.com:9403/#!/"]')
                await self.page.wait_for_timeout(5000)
                print("Filling form fields in iframe...")
                    
                # Fill Seleccionar Tienda
                store_selector = iframe.locator('select#Tienda')
                await store_selector.wait_for(state="visible", timeout=10000)
                await store_selector.select_option(value="2015")
                print("Store selected successfully")
                    
                # Fill Número de Ticket
                ticket_input = iframe.locator('input#ticket')
                await ticket_input.wait_for(state="visible", timeout=10000)
                await ticket_input.fill("12345")
                print("Ticket number filled successfully")
                    
                # Fill Total
                total_input = iframe.locator('input#total')
                await total_input.wait_for(state="visible", timeout=10000)
                await total_input.fill("67.89")
                print("Total amount filled successfully")
                await self.page.wait_for_timeout(2000)
                    
                # Click Buscar Ticket button
                buscar_ticket_button = iframe.locator('button.btn.btn-primary.button-principal:has-text("Buscar Ticket")')
                await buscar_ticket_button.wait_for(state="visible", timeout=10000)
                    
                # Click in Buscar Ticket button
                await buscar_ticket_button.click()
                print("Clicked on 'Buscar Ticket' button")
                    
                await self.page.wait_for_timeout(3000)
                
            except Exception as e:
                print(f"Error interacting with button: {e}")


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