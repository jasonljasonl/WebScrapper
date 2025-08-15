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

reference_locator = ''

@pytest.mark.asyncio
async def test_cdiscount_product_rate():
    global reference_locator
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()

    await page.goto('https://www.cdiscount.com/telephonie/telephone-mobile/samsung-galaxy-a14-5g-noir-64-go/f-14404-sam8806094825374.html')

    await page.locator("button[data-id='description-accordion']").click()
    reference_locator = await page.locator("//tr[th[normalize-space()='Référence']]/td").inner_text()
    print(reference_locator)

    await page.locator("button[data-id='avis-accordion']").click()
    await page.wait_for_timeout(1000)

    await page.wait_for_selector("li[data-url*='starValueList=1']")
    await page.locator("li[data-url*='starValueList=1']").click()
    await asyncio.sleep(1)


    while True:
        await page.wait_for_selector("li.c-customer-reviews__item")
        comments = await page.locator('div.c-customer-review__content').all()

        next_button = page.locator("input[value='Suivant']").first

        print(len(comments))

        for i,comment in enumerate(comments):
            comment_text = await comment.locator("p").inner_text()
            print(f"\nComments #{i+1}:\n{comment_text}")

        button_disabled = await next_button.get_attribute("disabled")
        if button_disabled is not None:
            break

        if await next_button.count() == 0:
            break

        await next_button.click()
        await page.wait_for_timeout(1000)

    return playwright, browser, context, page

@pytest.mark.asyncio
async def test_amazon_product_rate():
    auth_path = os.path.abspath("../playwright/.auth/auth.json")
    playwright, browser, context, page = await open_logged_in(auth_path)

    await test_cdiscount_product_rate()

    await page.goto('https://www.amazon.fr/')
    await page.locator("input#twotabsearchtextbox").fill(reference_locator)
    await page.locator("input#nav-search-submit-button").click()

    await page.wait_for_selector("div[role='listitem']")
    not_sponsored_item = page.locator("div:not(:has(a.puis-sponsored-label-text)) div[data-cy='title-recipe']")
    await not_sponsored_item.first.click()

    await page.wait_for_selector("a[data-hook='see-all-reviews-link-foot']")

    await page.locator("a[data-hook='see-all-reviews-link-foot']").first.click()

    await page.wait_for_selector("a[href*='filterByStar=one_star']")
    await page.locator("a[href*='filterByStar=one_star']").click()
    await page.wait_for_timeout(1000)

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


