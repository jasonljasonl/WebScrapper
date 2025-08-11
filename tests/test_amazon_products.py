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

    await page.goto('https://www.amazon.fr/Lepro-Dimmable-Puissant-R%C3%A9glable-Anti-%C3%89blouissement/dp/B095R8KFN3/?_encoding=UTF8&pd_rd_w=kBpcM&content-id=amzn1.sym.678de850-ec61-45a5-ac60-3d5045978e5b%3Aamzn1.symc.9b8fba90-e74e-4690-b98f-edc36fe735a6&pf_rd_p=678de850-ec61-45a5-ac60-3d5045978e5b&pf_rd_r=Q4JK90TKZKXNNQC37GC7&pd_rd_wg=klq0l&pd_rd_r=889d0cf8-3f95-41a8-bea1-a26a5e7bdbbe&ref_=pd_hp_d_btf_ci_mcx_mr_ca_id_hp_d&th=1')

    await page.locator("a[data-hook='see-all-reviews-link-foot']").first.click()

    await page.wait_for_selector("a[href*='filterByStar=one_star']")
    await page.locator("a[href*='filterByStar=one_star']").click()

    await page.locator('li.a-last').click()

    await page.wait_for_load_state("load")

    while True:
        await page.wait_for_selector("li[data-hook='review']")

        comments = await page.locator("li[data-hook='review']").all()

        next_button_li = page.locator('li.a-last')
        li_class = await next_button_li.get_attribute('class')

        if li_class and 'a-disabled' in li_class:
            break

        print(len(comments))

        for i, comment in enumerate(comments):
            comment_text = await comment.locator("span[data-hook='review-body']").inner_text()
            print(f"\nComments #{i+1}:\n{comment_text}")
        await next_button_li.click()


if __name__ == "__main__":
    asyncio.run(test_get_product_rate())
