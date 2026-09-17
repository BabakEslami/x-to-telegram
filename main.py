import os
import feedparser
import requests

RSS_URL = "https://rss.app/r/feed/jvD8rKGmaLaY0OMs"

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

feed = feedparser.parse(RSS_URL)

print("Feed title:", feed.feed.get("title", ""))
print("Entries:", len(feed.entries))

if not feed.entries:
    raise SystemExit("No RSS entries found")

entry = feed.entries[0]

title = entry.get("title", "").strip()
link = entry.get("link", "").strip()
summary = entry.get("summary", "").strip()

message = ""

if title:
    message += title

if summary and summary != title:
    if message:
        message += "\n\n"
    message += summary

if link:
    if message:
        message += "\n\n"
    message += link

telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

response = requests.post(
    telegram_url,
    data={
        "chat_id": CHAT_ID,
        "text": message,
        "disable_web_page_preview": False,
    },
    timeout=30,
)

print("Telegram status:", response.status_code)
print(response.text)
