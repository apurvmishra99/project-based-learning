import praw

reddit = praw.Reddit(client_id= '',
                    client_secret= '',
                    password= '',
                    username= '',
                    user_agent= ''
                    )

subreddit = reddit.subreddit("")
print(reddit.user.me())
for submission in subreddit.new(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("-------------------------------------------------------------------------------------\n")
    
