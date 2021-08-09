import asyncio
import discord
import json
import logging

from typing import Optional

from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash import SlashContext
from discord_slash.model import SlashCommandOptionType
from discord_slash.utils.manage_commands import create_option


log = logging.getLogger(__name__)


bot = commands.Bot(command_prefix="/", intents=discord.Intents.default())
commands = SlashCommand(bot, sync_commands=True)


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
