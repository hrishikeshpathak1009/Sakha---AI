from browser import (
    open_website,
    search_youtube,
    play_first_video
)


def browser_open_website(url):
    open_website(url)

    return f"Opened the requested site"


def browser_search_youtube(query):
    search_youtube(query)

    return f"Searched YouTube for: {query}"


def browser_play_first_video():
    play_first_video()

    return "Played the first YouTube video."