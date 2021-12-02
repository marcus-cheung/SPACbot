import praw

reddit = praw.Reddit(
    client_id="pgXw268OBsjmAQ",
    client_secret="XRZIHO0U23CplRr9ASjFkS9__vLp3w",
    password="1limabeaN",
    user_agent="Reddit WebScraping",
    username="thecooldudie3",
)

latest_posts = reddit.subreddit("SPACs").new(limit=1)
for post in latest_posts:
    latest_post = post


def getNew():
    newest = reddit.subreddit("SPACs").new(limit=1)
    for post in newest:
        return post


def RedditDA():
    global latest_post
    newpost = getNew()
    flair = newpost.link_flair_text
    if latest_post != newpost and (
        flair == "Definitive Agreement" or flair == "Target Acquired!" or flair == "Rumor"
    ):
        latest_post = newpost
        return "@here" + newpost.url
    latest_post = newpost
    return ""