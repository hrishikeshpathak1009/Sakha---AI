from playwright.async_api import async_playwright


playwright = None
context = None
page = None


# ============================================================
# START BROWSER
# ============================================================

async def start_browser():

    global playwright
    global context
    global page

    if context is not None:

        try:

            if not context.is_closed():

                if page is None or page.is_closed():
                    page = await context.new_page()

                return

        except Exception:
            pass

    print("Starting SAAKHAA browser...")

    playwright = await async_playwright().start()

    context = await playwright.chromium.launch_persistent_context(
        user_data_dir="./saakhaa_browser_data",
        headless=False
    )

    if context.pages:
        page = context.pages[0]
    else:
        page = await context.new_page()

    print("SAAKHAA browser started.")


# ============================================================
# ENSURE BROWSER
# ============================================================

async def ensure_browser():

    global page

    if context is None or page is None:

        await start_browser()
        return

    try:

        if context.is_closed() or page.is_closed():
            await start_browser()

    except Exception:

        await start_browser()


# ============================================================
# OPEN WEBSITE
# ============================================================

async def open_website(url):

    await ensure_browser()

    await page.goto(
        url,
        wait_until="domcontentloaded"
    )

    print(f"Opened: {url}")

    return f"Opened {url}"


# ============================================================
# SEARCH YOUTUBE
# ============================================================

async def search_youtube(query):

    await ensure_browser()

    await page.goto(
        "https://www.youtube.com",
        wait_until="domcontentloaded"
    )

    search_box = page.get_by_role(
        "combobox",
        name="Search"
    )

    await search_box.fill(query)

    await search_box.press("Enter")

    await page.wait_for_load_state(
        "domcontentloaded"
    )

    print(
        f"YouTube search completed: {query}"
    )

    return f"Searched YouTube for {query}"


# ============================================================
# PLAY FIRST VIDEO
# ============================================================

async def play_first_video():

    await ensure_browser()

    first_video = page.locator(
        "ytd-video-renderer a#video-title"
    ).first

    await first_video.click()

    print(
        "Playing the first YouTube video."
    )

    return "Playing the first YouTube video."

# ============================================================
# SKIP YOUTUBE AD
# ============================================================
async def is_ad_playing():

    await ensure_browser()

    ad = page.locator(
        ".video-ads.ytp-ad-module"
    )

    return await ad.is_visible()


async def skip_ad():

    await ensure_browser()

    skip_button = page.locator(
        ".ytp-ad-skip-button, .ytp-ad-skip-button-modern"
    ).first

    try:

        await skip_button.wait_for(
            state="visible",
            timeout=10000
        )

        await skip_button.click()

        print("YouTube ad skipped.")

        return "Advertisement skipped."

    except Exception:

        print("No skippable advertisement found.")

        return "No skippable advertisement found."

async def handle_ad():

    if await is_ad_playing():

        print("Advertisement detected.")

        await skip_ad()

    else:

        print("No advertisement.")


# ============================================================
# CLOSE BROWSER
# ============================================================

async def close_browser():

    global playwright
    global context
    global page

    try:

        if context is not None:
            await context.close()

    except Exception:
        pass

    try:

        if playwright is not None:
            await playwright.stop()

    except Exception:
        pass

    context = None
    page = None
    playwright = None

    print("SAAKHAA browser closed.")

    return "Browser closed."