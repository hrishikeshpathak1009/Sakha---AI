
import asyncio

from browser import (
    start_browser,
    open_website,
    close_browser,
)


async def main():
    try:
        await start_browser()
        await open_website("https://www.youtube.com")

        input("Press Enter to close the browser...")

    finally:
        await close_browser()


if __name__ == "__main__":
    asyncio.run(main())
