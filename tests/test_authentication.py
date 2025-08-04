import os

from playwright.sync_api import sync_playwright


def test_get_authenticate():
    auth_path = os.path.abspath("../playwright/.auth/auth.json")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state=auth_path)
        page = context.new_page()
        page.goto("https://www.amazon.fr/")

        print("✅ Title:", page.title())

        assert "Bonjour" in page.content()
        browser.close()


