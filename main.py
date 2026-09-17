import os
import requests
from tweetkit_x import TweetKit

X_USERNAME = "melatonin38"

X_AUTH_TOKEN = os.environ["X_AUTH_TOKEN"]
X_CT0 = os.environ["X_CT0"]

TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

cookie = f"auth_token={X_AUTH_TOKEN}; ct0={X_CT0}"

tk = TweetKit(cookie=cookie)

tweets = tk.get_tweets(
    username=X_USERNAME,
    limit=5
)

print(f"Found {len(tweets)} tweets")

for tweet in tweets:
    print(tweet)
