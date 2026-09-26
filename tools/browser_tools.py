from browser import (
    open_website,
    search_youtube,
    play_first_video,
    close_browser,
)


async def browser_open_website(url):
    return await open_website(url)


async def browser_search_youtube(query):
    return await search_youtube(query)


async def browser_play_first_video():
    return await play_first_video()


async def browser_close():
    return await close_browser()


BROWSER_TOOLS = {
    "browser_open_website": browser_open_website,
    "browser_search_youtube": browser_search_youtube,
    "browser_play_first_video": browser_play_first_video,
    "browser_close": browser_close,
}