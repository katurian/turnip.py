import praw
import time
from time import sleep
import random
import re

def reply():
    replies = ["Hey there! I would love an invite. I also tip 15%.", "May I come in? Thank you!! I will happily tip 15%!", "Please invite me if you get a chance! I tip well.", "Looking to sell, thanks.", "Hi! Would love to join!", "Interested in selling!!", "Heyyyy I have an inventory of turnips I need to get rid of! I will share my profits too.", "Thank you for doing this, let me know if I can get an invite.", "Would very much appreciate it if you let me sell."] 
    return replies[random.randint(0, len(replies)-1)]

reddit = praw.Reddit(client_id='PFyXXXXXXXXXX',
                     client_secret='wIQgqpXXXXXXXXXXXXXXXXXXXXX',
                     user_agent='windows:turnip (by u/caturian)',
                     username='catXXXXX',
                     password='KXXXXXXXX')

state = False
ids=[]
while state == False:
    for submission in reddit.subreddit('acturnips').new(limit=10):
        timestamp = (time.time()-submission.created_utc)/60
        if (timestamp < 15 and timestamp > 2) and "buying" in submission.title and submission.id not in ids and int(re.findall("\d+", submission.title)[0]) > 350:
            submission.reply(reply())
            ids.append(submission.id)
            sleep(random.randint(6, 15))
        else:
            sleep(4)
            
