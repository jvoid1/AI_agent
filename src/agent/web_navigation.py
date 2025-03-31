from playwright.sync_api import sync_playwright

class WebNavigator:
    def __init__(self, urls):
        self.urls = urls

    def navigate_to_billing_section(self, browser):
        for url in self.urls:
            page = browser.new_page()
            page.goto(url)
            if self._locate_billing_section(page):
                return page
            page.close()
        return None

    def _locate_billing_section(self, page):
        try:
            billing_section = page.query_selector("selector-for-billing-section")
            if billing_section:
                billing_section.click()
                return True
        except Exception as e:
            print(f"Error locating billing section: {e}")
        return False

    def fill_invoice_form(self, page, form_data):
        try:
            page.fill("selector-for-invoice-field", form_data['invoice_field'])
            page.click("selector-for-submit-button")
        except Exception as e:
            print(f"Error filling invoice form: {e}")

def run_web_navigation(urls, form_data):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        navigator = WebNavigator(urls)
        page = navigator.navigate_to_billing_section(browser)
        if page:
            navigator.fill_invoice_form(page, form_data)
            page.close()
        browser.close()