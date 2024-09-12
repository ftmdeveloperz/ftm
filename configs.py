# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = os.environ.get("API_ID", "28776072")
    API_HASH = os.environ.get("API_HASH", "b3a786dce1f4e7d56674b7cadfde3c9d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7037453058:AAGDtxFckOjQryf7pwPVK7zdiMSW-vL6w6s")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Video-Merge-Bot")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002471632904")
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1002392831227")
    DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
    TIME_GAP = int(os.environ.get("TIME_GAP", 5))
    MAX_VIDEOS = int(os.environ.get("MAX_VIDEOS", 30))
    STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME", "0a578760a5a837896f60")
    STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS", "2qJoVG3wLqSZwkr")
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://ftm:ftm@ftmbot.z5iox.mongodb.net/?retryWrites=true&w=majority&appName=ftmbot")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "7042535787"))

    START_TEXT = """
Hi {name}, I am Video Merge Bot!
I can Merge Multiple Videos in One Video. Video Formats should be same.

Made with by @ftmdeveloper
"""
    CAPTION = "Video Merged by @{}\n\n Made with 💕 by @ftmdeveloper"
    PROGRESS = """
Percentage : {0}%
Done: {1}
Total: {2}
Speed: {3}/s
ETA: {4}
"""
