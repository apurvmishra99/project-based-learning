#! /home/apu35711/anaconda3/bin/python

import praw
import pdb
import os
import re

reddit = praw.Reddit(client_id= 'VgSmXEQw217mCQ',
                    client_secret= 'NzILPGFnOfRZRJ23FKoIOX8_M10',
                    password= 'dps12345@1',
                    username= 'gen2irony',
                    user_agent= 'PyBot 0.1'
                    )
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))


subreddit = reddit.subreddit("pythonforengineers")
for submission in subreddit.new(limit=15):
    if submission.id not in posts_replied_to:
        if re.search("I love python",submission.title, re.IGNORECASE):
            submission.reply("Me too!")
            print("Bot replying to:", submission.title)
            posts_replied_to.append(submission.id)

with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n") 
