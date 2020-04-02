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
    replies = ["Hey there! I would love an invite.", "May I come in? Thank you!! I will happily tip!", "Please invite me if you get a chance! I tip well.", "Looking for an invite, thanks.", "Hi! Would love to join!", "Interested!!", "I will share some of my profits :).", "Thank you for doing this, let me know if I can get an invite.", "Would very much appreciate it if you invited me."] 
    return replies[random.randint(0, len(replies)-1)]

def sell(postLimit, price, minutesMin, minutesMax):
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
              sleep(2)
              
def buy(postLimit, price, minutesMin, minutesMax):
  state = False
  ids=[]
  while state == False:
      for submission in reddit.subreddit('acturnips').new(limit=postLimit):
          timestamp = (time.time()-submission.created_utc)/60
          if (timestamp < minutesMax and timestamp > minutesMin) and ("selling" in submission.title) and (submission.id not in ids) and (int(re.findall("\d+", submission.title)[0]) < price):
              submission.reply(reply())
              ids.append(submission.id)
              sleep(random.randint(4, 8))
          else:
              sleep(2)
