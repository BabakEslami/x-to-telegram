import requests

RSS_URL = "https://rss.app/r/feed/jvD8rKGmaLaY0OMs"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/153.0.0.0 Safari/537.36"
    ),
    "Accept": (
        "application/rss+xml, application/xml, text/xml, "
        "text/html, application/xhtml+xml"
    ),
}

response = requests.get(
    RSS_URL,
    headers=headers,
    timeout=30,
    allow_redirects=True,
)

print("Status:", response.status_code)
print("Final URL:", response.url)
print("Content-Type:", response.headers.get("content-type"))
print("Length:", len(response.content))
print()
print(response.text[:3000])
