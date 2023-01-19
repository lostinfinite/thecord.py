from __future__ import annotations
from typing import Optional
from typing_extensions import Annotated

import discord
from discord import app_commands
from discord.ext import commands

import pytest

def test_annotated_annotation():
    # can't exactly test if the parameter is the same, so just test if it raises something
    @app_commands.command()
    async def foo(interaction: discord.Interaction, param: Annotated[float, Optional[int]]):
        pass


    def to_hex(arg: str) -> int:
        return int(arg, 16)

    class Flag(commands.FlagConverter):
        thing: Annotated[int, to_hex]

    assert Flag.get_flags()['thing'].annotation == to_hex

    @commands.command()
    async def bar(ctx: commands.Context, param: Annotated[float, Optional[int]]):
        pass

    assert bar.clean_params['param'].annotation == Optional[int]

    @commands.command()
    async def nested(ctx: commands.Context, param: Optional[Annotated[str, int]]):
        pass

    assert nested.clean_params['param'].annotation == Optional[int]
