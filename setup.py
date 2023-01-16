from setuptools import setup, find_packages

setup(
    name="thecord.py",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "discord.py"
    ],
    author="DCA Utilites",
    author_email="support@dcaus.cf",
    description="Just like discord.py but it has slash commands???!!!",
    url="https://github.com/DCAus-code/thecord.py",
)
