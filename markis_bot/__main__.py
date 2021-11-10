import asyncio
import os
import logging
import signal
import sys
from typing import List

from discord_slash.utils.manage_commands import remove_all_commands
from markis_bot.bot import run_bot
from markis_bot.bot import stop_bot


DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
DISCORD_BOT_ID = os.environ.get("DISCORD_BOT_ID")

log = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def main():
    if not DISCORD_TOKEN:
        raise ValueError("DISCORD_TOKEN is invalid")
    if not DISCORD_BOT_ID:
        raise ValueError("DISCORD_BOT_ID is invalid")

    signal.signal(signal.SIGINT, exit)
    signal.signal(signal.SIGTERM, exit)

    log.info("Removing all commands")
    asyncio.run(remove_all_commands(DISCORD_BOT_ID, DISCORD_TOKEN))

    log.info("Markis-Bot starting")
    run_bot(DISCORD_TOKEN)


def exit(signum, frame):
    log.info(f"Markis-Bot stopping ({signum}, {frame})")
    stop_bot()


if __name__ == "__main__":
    main()
