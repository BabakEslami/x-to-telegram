import os
from playwright.sync_api import sync_playwright

X_USERNAME = "melatonin38"

AUTH_TOKEN = os.environ["X_AUTH_TOKEN"]
CT0 = os.environ["X_CT0"]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    context = browser.new_context()

    context.add_cookies([
        {
            "name": "auth_token",
            "value": AUTH_TOKEN,
            "domain": ".x.com",
            "path": "/",
            "httpOnly": True,
            "secure": True,
        },
        {
            "name": "ct0",
            "value": CT0,
            "domain": ".x.com",
            "path": "/",
            "secure": True,
        },
    ])

    page = context.new_page()

    url = f"https://x.com/{X_USERNAME}"
    print("Opening:", url)

    page.goto(url, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(8000)

    print("Page title:", page.title())

    articles = page.locator("article")
    count = articles.count()

    print("Found articles:", count)

    for i in range(min(count, 5)):
        text = articles.nth(i).inner_text()
        print("\n--- POST", i + 1, "---")
        print(text[:1500])

    browser.close()
