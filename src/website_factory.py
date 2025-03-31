from src.agent.websites.dath_website import DathWebsite
from src.agent.websites.monparis_website import MonparisWebsite
from src.agent.websites.alsea_website import AlseaWebsite

class WebsiteFactory:
    @staticmethod
    def create_website(website_type: str, page, config: dict):
        websites = {
            "dath": DathWebsite,
            "monparis": MonparisWebsite,
            "alsea": AlseaWebsite
        }
        
        website_class = websites.get(website_type.lower())
        if not website_class:
            raise ValueError(f"Unsupported website type: {website_type}")
            
        return website_class(page, config)