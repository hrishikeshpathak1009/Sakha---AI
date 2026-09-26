from browser import (
    search_youtube,
    play_first_video,
    youtube_pause as youtube_pause_action,
    youtube_resume as youtube_resume_action,
    youtube_skip_forward as youtube_skip_forward_action,
    youtube_skip_backward as youtube_skip_backward_action,
    youtube_next as youtube_next_action,
    youtube_previous as youtube_previous_action,
    youtube_mute as youtube_mute_action,
    youtube_unmute as youtube_unmute_action,
    youtube_fullscreen as youtube_fullscreen_action,
    youtube_exit_fullscreen as youtube_exit_fullscreen_action,
    youtube_skip_ad as youtube_skip_ad_action,
)


# =========================================================
# YOUTUBE SEARCH
# =========================================================

async def youtube_search(query: str):
    """
    Search YouTube for the requested video, song, topic, or content.

    Use ONLY when the user explicitly asks to search or find
    something on YouTube.

    Examples:
    "Search YouTube for Krishna bhajans"
    "Find Python tutorials on YouTube"
    "Look for Arijit Singh songs on YouTube"

    Do NOT use this tool for ordinary questions or general web searches.
    """

    return await search_youtube(query)


# =========================================================
# PLAY VIDEO
# =========================================================

async def youtube_play():
    """
    Play the first video from the current YouTube search results.

    Use ONLY when the user explicitly asks to:
    - play the video
    - play the first result
    - start the selected YouTube video

    Usually this should be used after youtube_search.
    """

    return await play_first_video()


# =========================================================
# PAUSE
# =========================================================

async def youtube_pause():
    """
    Pause the currently playing YouTube video.

    Use ONLY when the user explicitly asks to:
    - pause the video
    - pause YouTube
    - stop the video temporarily

    Do NOT interpret the global SAAKHAA command "stop" as
    a request to pause YouTube.
    """

    return await youtube_pause_action()


# =========================================================
# RESUME
# =========================================================

async def youtube_resume():
    """
    Resume a paused YouTube video.

    Use ONLY when the user explicitly asks to:
    - resume the video
    - continue playing
    - continue the video
    - play the paused video
    """

    return await youtube_resume_action()


# =========================================================
# SKIP FORWARD
# =========================================================

async def youtube_skip_forward(seconds: int = 10):
    """
    Skip forward in the currently playing YouTube video.

    Use ONLY when the user explicitly asks to move forward
    or skip ahead in the video.

    Examples:
    "Skip forward"
    "Skip 10 seconds"
    "Go forward 30 seconds"
    "Move ahead one minute"

    The seconds parameter specifies how many seconds to skip.
    """

    return await youtube_skip_forward_action(seconds)


# =========================================================
# SKIP BACKWARD
# =========================================================

async def youtube_skip_backward(seconds: int = 10):
    """
    Skip backward in the currently playing YouTube video.

    Use ONLY when the user explicitly asks to:
    - go back in the video
    - rewind
    - skip backward

    Examples:
    "Go back 10 seconds"
    "Rewind 30 seconds"
    "Skip backward"

    The seconds parameter specifies how many seconds to go back.
    """

    return await youtube_skip_backward_action(seconds)


# =========================================================
# NEXT VIDEO
# =========================================================

async def youtube_next():
    """
    Move to the next YouTube video.

    Use ONLY when the user explicitly asks:
    - next video
    - play the next video
    - skip to the next video
    """

    return await youtube_next_action()


# =========================================================
# PREVIOUS VIDEO
# =========================================================

async def youtube_previous():
    """
    Move to the previous YouTube video.

    Use ONLY when the user explicitly asks:
    - previous video
    - go to the previous video
    - play the previous video
    """

    return await youtube_previous_action()


# =========================================================
# MUTE
# =========================================================

async def youtube_mute():
    """
    Mute the currently playing YouTube video.

    Use ONLY when the user explicitly asks to:
    - mute YouTube
    - mute the video
    - silence the video
    """

    return await youtube_mute_action()


# =========================================================
# UNMUTE
# =========================================================

async def youtube_unmute():
    """
    Unmute the currently playing YouTube video.

    Use ONLY when the user explicitly asks to:
    - unmute YouTube
    - unmute the video
    - restore the video's sound
    """

    return await youtube_unmute_action()


# =========================================================
# FULLSCREEN
# =========================================================

async def youtube_fullscreen():
    """
    Put the current YouTube video into fullscreen mode.

    Use ONLY when the user explicitly asks to:
    - make the video fullscreen
    - enter fullscreen
    - fullscreen the video
    """

    return await youtube_fullscreen_action()


# =========================================================
# EXIT FULLSCREEN
# =========================================================

async def youtube_exit_fullscreen():
    """
    Exit YouTube fullscreen mode.

    Use ONLY when the user explicitly asks to:
    - exit fullscreen
    - leave fullscreen
    - return from fullscreen
    """

    return await youtube_exit_fullscreen_action()


# =========================================================
# SKIP AD
# =========================================================

async def youtube_skip_ad():
    """
    Attempt to skip a currently visible, skippable YouTube advertisement.

    Use ONLY when the user explicitly asks to:
    - skip the ad
    - skip the advertisement
    - skip the commercial

    Do NOT call this during normal video playback.

    If YouTube does not currently display a skippable advertisement,
    the tool reports that no skippable ad is available.
    """

    return await youtube_skip_ad_action()


# =========================================================
# TOOL REGISTRY
# =========================================================

YOUTUBE_TOOLS = {
    "youtube_search": youtube_search,
    "youtube_play": youtube_play,
    "youtube_pause": youtube_pause,
    "youtube_resume": youtube_resume,
    "youtube_skip_forward": youtube_skip_forward,
    "youtube_skip_backward": youtube_skip_backward,
    "youtube_next": youtube_next,
    "youtube_previous": youtube_previous,
    "youtube_mute": youtube_mute,
    "youtube_unmute": youtube_unmute,
    "youtube_fullscreen": youtube_fullscreen,
    "youtube_exit_fullscreen": youtube_exit_fullscreen,
    "youtube_skip_ad": youtube_skip_ad,
}