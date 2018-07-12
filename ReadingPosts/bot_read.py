import praw

reddit = praw.Reddit(client_id= 'VgSmXEQw217mCQ',
                    client_secret= 'NzILPGFnOfRZRJ23FKoIOX8_M10',
                    password= 'dps12345@1',
                    username= 'gen2irony',
                    user_agent= 'PyBot 0.1'
                    )

subreddit = reddit.subreddit("formula1")
print(reddit.user.me())
for submission in subreddit.new(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("-------------------------------------------------------------------------------------\n")
    
