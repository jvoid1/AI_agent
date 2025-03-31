from abc import ABC, abstractmethod
from playwright.async_api import Page

class BaseWebsite(ABC):
    def __init__(self, page: Page, config: dict):
        self.page = page
        self.config = config
        self.selectors = config.get("selectors", {})

    @abstractmethod
    async def navigate_to_billing(self):
        """Navigate to billing section"""
        pass

    @abstractmethod
    async def fill_form(self, form_data: dict):
        """Fill the billing form"""
        pass

    @abstractmethod
    async def submit_form(self):
        """Submit the form"""
        pass

    async def handle_errors(self, error: Exception):
        """Handle website-specific errors"""
        pass