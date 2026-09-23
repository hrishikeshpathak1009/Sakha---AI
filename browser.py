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

def search_youtube(query):
    global page

    if page is None:
        start_browser()

    # Open YouTube
    page.goto("https://www.youtube.com")

    # Find the search box
    search_box = page.get_by_role("combobox", name="Search")

    # Type the query
    search_box.fill(query)

    # Press Enter
    search_box.press("Enter")

    # Wait for results to load
    page.wait_for_load_state("domcontentloaded")

    print(f"YouTube search completed: {query}")

def play_first_video():
    global page

    if page is None:
        print("Browser is not running.")
        return

    first_video = page.locator(
        "ytd-video-renderer a#video-title"
    ).first

    first_video.click()

    print("Playing the first YouTube video.")


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