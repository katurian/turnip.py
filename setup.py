import praw
import time
from time import sleep
import random
import re

reddit = praw.Reddit(client_id='PFyJXXXXXXXX',
                     client_secret='wIQgqph3XXXXXXXXX',
                     user_agent='windows:turnip (by u/caturian)',
                     username='XXXXX',
                     password='XXXXXXX')

def reply():
    replies = ["Hey there! I would love an invite. I also tip 15%.", "May I come in? Thank you!! I will happily tip 15%!", "Please invite me if you get a chance! I tip well.", "Looking to sell, thanks.", "Hi! Would love to join!", "Interested in selling!!", "Heyyyy I have an inventory of turnips I need to get rid of! I will share my profits too.", "Thank you for doing this, let me know if I can get an invite.", "Would very much appreciate it if you let me sell."] 
    return replies[random.randint(0, len(replies)-1)]

def eval(postLimit, price, minutesMin, minutesMax):
  state = False
  ids=[]
  while state == False:
      for submission in reddit.subreddit('acturnips').new(limit=postLimit):
          timestamp = (time.time()-submission.created_utc)/60
          if (timestamp < minutesMax and timestamp > minutesMin) and ("buying" in submission.title) and (submission.id not in ids) and (int(re.findall("\d+", submission.title)[0]) > price):
              submission.reply(reply())
              ids.append(submission.id)
              sleep(random.randint(6, 10))
          else:
              sleep(4)
