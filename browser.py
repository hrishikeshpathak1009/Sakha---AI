from playwright.sync_api import sync_playwright

playwright = None
context = None
page = None


def start_browser():

    global playwright, context, page

    playwright = sync_playwright().start()

    context = playwright.chromium.launch_persistent_context(
        user_data_dir="./saakhaa_browser_data",
        headless=False
    )

    page = context.pages[0] if context.pages else context.new_page()

    print("SAAKHAA browser started.")


def open_website(url):

    if page is None:
        start_browser()

    page.goto(url)


def close_browser():

    global playwright, context, page

    if context:
        context.close()

    if playwright:
        playwright.stop()

    context = None
    page = None
    playwright = None

    print("SAAKHAA browser closed.")