from __future__ import annotations

from io import BytesIO

import discord


FILE = BytesIO()


def test_file_with_no_name():
    f = discord.File('.gitignore')
    assert f.filename == '.gitignore'


def test_io_with_no_name():
    f = discord.File(FILE)
    assert f.filename == 'untitled'


def test_file_with_name():
    f = discord.File('.gitignore', 'test')
    assert f.filename == 'test'


def test_io_with_name():
    f = discord.File(FILE, 'test')
    assert f.filename == 'test'


def test_file_with_no_name_and_spoiler():
    f = discord.File('.gitignore', spoiler=True)
    assert f.filename == 'SPOILER_.gitignore'
    assert f.spoiler == True


def test_file_with_spoiler_name_and_implicit_spoiler():
    f = discord.File('.gitignore', 'SPOILER_.gitignore')
    assert f.filename == 'SPOILER_.gitignore'
    assert f.spoiler == True


def test_file_with_spoiler_name_and_spoiler():
    f = discord.File('.gitignore', 'SPOILER_.gitignore', spoiler=True)
    assert f.filename == 'SPOILER_.gitignore'
    assert f.spoiler == True


def test_file_with_spoiler_name_and_not_spoiler():
    f = discord.File('.gitignore', 'SPOILER_.gitignore', spoiler=False)
    assert f.filename == '.gitignore'
    assert f.spoiler == False


def test_file_with_name_and_double_spoiler_and_implicit_spoiler():
    f = discord.File('.gitignore', 'SPOILER_SPOILER_.gitignore')
    assert f.filename == 'SPOILER_.gitignore'
    assert f.spoiler == True


def test_file_with_name_and_double_spoiler_and_spoiler():
    f = discord.File('.gitignore', 'SPOILER_SPOILER_.gitignore', spoiler=True)
    assert f.filename == 'SPOILER_.gitignore'
    assert f.spoiler == True


def test_file_with_name_and_double_spoiler_and_not_spoiler():
    f = discord.File('.gitignore', 'SPOILER_SPOILER_.gitignore', spoiler=False)
    assert f.filename == '.gitignore'
    assert f.spoiler == False


def test_file_with_spoiler_with_overriding_name_not_spoiler():
    f = discord.File('.gitignore', spoiler=True)
    f.filename = '.gitignore'
    assert f.filename == '.gitignore'
    assert f.spoiler == False


def test_file_with_spoiler_with_overriding_name_spoiler():
    f = discord.File('.gitignore', spoiler=True)
    f.filename = 'SPOILER_.gitignore'
    assert f.filename == 'SPOILER_.gitignore'
    assert f.spoiler == True


def test_file_not_spoiler_with_overriding_name_not_spoiler():
    f = discord.File('.gitignore')
    f.filename = '.gitignore'
    assert f.filename == '.gitignore'
    assert f.spoiler == False


def test_file_not_spoiler_with_overriding_name_spoiler():
    f = discord.File('.gitignore')
    f.filename = 'SPOILER_.gitignore'
    assert f.filename == 'SPOILER_.gitignore'
    assert f.spoiler == True


def test_file_not_spoiler_with_overriding_name_double_spoiler():
    f = discord.File('.gitignore')
    f.filename = 'SPOILER_SPOILER_.gitignore'
    assert f.filename == 'SPOILER_.gitignore'
    assert f.spoiler == True
