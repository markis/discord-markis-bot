import asyncio
import discord
import json
import logging
import os
import typing

from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash import SlashContext
from discord_slash.model import SlashCommandOptionType
from discord_slash.utils.manage_commands import create_option


log = logging.getLogger(__name__)


bot = commands.Bot(command_prefix="/", intents=discord.Intents.default())
commands = SlashCommand(bot, sync_commands=True)


def _get_discord_guild_ids() -> typing.Optional[typing.List[int]]:
    raw_env = os.environ.get("DISCORD_GUILD_ID")
    if not raw_env:
        return None

    return [int(val) for val in raw_env.split(",") if val]


@commands.slash(
    name="compliment",
    description="Feeling down? This might be just the pick-me-up you need!",
    options=[
        create_option(
            name="name",
            description="Optional name of user to compliment",
            option_type=SlashCommandOptionType.USER,
            required=False,
        )
    ],
    guild_ids=_get_discord_guild_ids(),
)
async def compliment(ctx: SlashContext, name = None, *args, **kwargs):
    log.info("Handing compliment")
    log.info(json.dumps(name), extra={"args": args, "kwargs": kwargs})

    name = getattr(ctx.author, "name", "")
    await ctx.send(content=f"you look nice today, {name}")


def run_bot(token: str):
    bot.run(token)


def stop_bot():
    asyncio.run(bot.close())
