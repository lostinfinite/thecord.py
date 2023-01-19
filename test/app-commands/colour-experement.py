
from __future__ import annotations

import discord
import pytest


@pytest.mark.parametrize(
    ('value', 'expected'),
    [
        ('0xFF1294', 0xFF1294),
        ('0xff1294', 0xFF1294),
        ('0xFFF', 0xFFFFFF),
        ('0xfff', 0xFFFFFF),
        ('#abcdef', 0xABCDEF),
        ('#ABCDEF', 0xABCDEF),
        ('#ABC', 0xAABBCC),
        ('#abc', 0xAABBCC),
        ('rgb(68,36,59)', 0x44243B),
        ('rgb(26.7%, 14.1%, 23.1%)', 0x44243B),
        ('rgb(20%, 24%, 56%)', 0x333D8F),
        ('rgb(20%, 23.9%, 56.1%)', 0x333D8F),
        ('rgb(51, 61, 143)', 0x333D8F),
    ],
)
def test_from_str(value, expected):
    assert discord.Colour.from_str(value) == discord.Colour(expected)


@pytest.mark.parametrize(
    ('value'),
    [
        'not valid',
        '0xYEAH',
        '#YEAH',
        '#yeah',
        'yellow',
        'rgb(-10, -20, -30)',
        'rgb(30, -1, 60)',
        'invalid(a, b, c)',
        'rgb(',
    ],
)
def test_from_str_failures(value):
    with pytest.raises(ValueError):
        discord.Colour.from_str(value)
