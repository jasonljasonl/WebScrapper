from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.amazon.fr/-/en/ref=nav_logo")

        context.storage_state(path="auth.json")

        browser.close()

if __name__ == "__main__":
    run()
