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

    await page.goto('https://www.amazon.fr/dp/B0BSV9SG7B/ref=sspa_dk_detail_3?pd_rd_i=B0BSV9SG7B&pd_rd_w=UEtYH&content-id=amzn1.sym.d28e3d6a-4412-4be7-a4f8-1c4a85ce86d9&pf_rd_p=d28e3d6a-4412-4be7-a4f8-1c4a85ce86d9&pf_rd_r=WXZV2AC40WY78SCS7DXA&pd_rd_wg=4HOaI&pd_rd_r=557db566-dbe9-43e1-8ca0-24421e832a82&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw&th=1')

    await page.locator("a[data-hook='see-all-reviews-link-foot']").first.click()

    await page.wait_for_selector("a[href*='filterByStar=one_star']")
    await page.locator("a[href*='filterByStar=one_star']").click()


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


        await next_button.click()
        await page.wait_for_load_state("load")


if __name__ == "__main__":
    asyncio.run(test_get_product_rate())
