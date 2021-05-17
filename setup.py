from distutils.core import setup

setup(
    name="teleframe",
    packages=["teleframe"],
    version="0.3.5",
    license="MIT",
    description="Simple python module for Telegram Bot API Webhooks.",
    author="speedssster",
    author_email="lastprogamer0@gmail.com",
    url="https://github.com/Speedssster/teleframe",
    download_url="https://github.com/Speedssster/teleframe/archive/0.3.5.tar.gz",
    keywords=["telegram_bot", "API", "webhooks"],
    install_requires=["requests"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
)
