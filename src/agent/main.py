import json
import asyncio
from playwright.async_api import async_playwright
from src.website_factory import WebsiteFactory

async def main():
    # Load configurations
    with open('src/config/settings.json') as f:
        settings = json.load(f)

    try:
        async with async_playwright() as p:
            # Launch browser in headless mode
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                record_video_dir="videos/",
                viewport={'width': 1920, 'height': 1080}
            )
            page = await context.new_page()

            for website_config in settings["websites"]:
                try:
                    # Create website handler
                    website = WebsiteFactory.create_website(
                        website_config["type"],
                        page,
                        website_config
                    )

                    # Navigate to website URL first
                    await page.goto(website_config["url"])
                    print(f"Navigating to {website_config['url']}")
                    await page.goto(website_config["url"])

                    # Execute website workflow
                    print(f"Processing website: {website_config['name']}")
                    await website.navigate_to_billing()
                    #await website.fill_form(website_config["form_data"])
                    #await website.submit_form()
                    

                except Exception as e:
                    print(f"Error processing website {website_config['name']}: {str(e)}")
                    await website.handle_errors(e)

            await context.close()
            await browser.close()

    except Exception as e:
        print(f"Fatal error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())