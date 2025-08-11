import os
import pytest
from playwright.async_api import async_playwright
import asyncio


@pytest.mark.asyncio
async def test_get_product_rate():
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()

    await page.goto('https://www.cdiscount.com/electromenager/preparation-culinaire/moulinex-hf452110-clickchef-robot-cuiseur-multifon/f-110220101-auc3016661157936.html#mpos=0|mp')

    await page.locator("button[data-id='avis-accordion']").click()

    await page.wait_for_selector("li[data-url*='starValueList=1']")
    await page.locator("li[data-url*='starValueList=1']").click()

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
        else:
            await next_button.click()

    return playwright, browser, context, page

