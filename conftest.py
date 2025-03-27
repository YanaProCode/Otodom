import pytest
from playwright.sync_api import sync_playwright


def before_suite(request):
    browser_type = request.param
    with sync_playwright() as p:
        browser = getattr(p, browser_type).launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        #stealth_sync(page)
        yield page
        browser.close()