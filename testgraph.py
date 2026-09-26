import asyncio

from graph import ask_saakhaa
from tools import TOOL_FUNCTIONS


print("\nAVAILABLE TOOLS:")
for tool in TOOL_FUNCTIONS:
    print(" -", tool)


async def main():

    while True:

        text = input("\nYou: ").strip()

        if text.lower() in {
            "exit",
            "quit",
            "stop"
        }:
            break

        response = await ask_saakhaa(
            text,
            thread_id="test"
        )

        print("SAAKHAA:", response)


if __name__ == "__main__":
    asyncio.run(main())