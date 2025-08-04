import os
import re

import pytest
from playwright.async_api import async_playwright
from playwright.sync_api import Page, expect, sync_playwright
import asyncio

from pytest_playwright.pytest_playwright import playwright

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
    print(page.title())

    await page.locator("a[data-hook='see-all-reviews-link-foot']").first.click()
    print(page.title())

    comments = await page.locator("li[data-hook='review']").all()

    for comment in comments:
        print(await comment.text_content())

    await browser.close()
    await playwright.stop()

if __name__ == "__main__":
    asyncio.run(test_get_product_rate())
