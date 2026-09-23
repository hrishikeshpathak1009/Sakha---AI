from .browser_tools import (
    browser_open_website,
    browser_search_youtube,
    browser_play_first_video
)

from .system_tools import (
    get_current_time,
    get_current_date,
    open_application
)


TOOL_FUNCTIONS = {
    "browser_open_website": browser_open_website,
    "browser_search_youtube": browser_search_youtube,
    "browser_play_first_video": browser_play_first_video,

    "get_current_time": get_current_time,
    "get_current_date": get_current_date,
    "open_application": open_application
}