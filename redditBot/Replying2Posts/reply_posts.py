#! /home/apu35711/anaconda3/bin/python

import praw
import pdb
import os
import re

reddit = praw.Reddit(client_id= '',
                    client_secret= '',
                    password= '',
                    username= '',
                    user_agent= ''
                    )
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))


subreddit = reddit.subreddit("")
for submission in subreddit.new(limit=15):
    if submission.id not in posts_replied_to:
        if re.search("",submission.title, re.IGNORECASE):
            submission.reply("")
            print("Bot replying to:", submission.title)
            posts_replied_to.append(submission.id)

with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n") 
