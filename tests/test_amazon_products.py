import os
import pytest
from playwright.async_api import async_playwright
import asyncio

AUTH_PATH = os.path.abspath("../playwright/.auth/auth.json")

async def open_logged_in(auth_path):
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context(storage_state=auth_path)
    page = await context.new_page()
    return playwright, browser, context, page

@pytest.mark.asyncio
async def test_get_product_rate():
    auth_path = os.path.abspath("../playwright/.auth/auth.json")
    playwright, browser, context, page = await open_logged_in(auth_path)

    await page.goto('https://www.amazon.fr/-/en/Moulinex-Click-Chef-HF452110-Processor/dp/B089QQM45F/ref=cm_cr_arp_d_bdcrb_top?ie=UTF8')

    await page.locator("a[data-hook='see-all-reviews-link-foot']").first.click()

    await page.wait_for_selector("a[href*='filterByStar=one_star']")
    await page.locator("a[href*='filterByStar=one_star']").click()
    await asyncio.sleep(2)

    await page.wait_for_load_state("load")

    while True:
        await page.wait_for_selector("li[data-hook='review']")

        comments = await page.locator("li[data-hook='review']").all()
        print(len(comments))

        for i, comment in enumerate(comments):
            comment_text = await comment.locator("span[data-hook='review-body']").inner_text()
            print(f"\nComments #{i + 1}:\n{comment_text}")

        next_button = page.locator('li.a-last')

        if await next_button.count() == 0:
            break

        li_class = await next_button.get_attribute('class')
        if li_class and 'a-disabled' in li_class:
            break

        if next_button.count != 0:
            await next_button.click()
        await page.wait_for_load_state("load")


if __name__ == "__main__":
    asyncio.run(test_get_product_rate())
