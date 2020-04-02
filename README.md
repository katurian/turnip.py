# turnip.py
PRAW functions that reply to ``x`` number of submissions on https://www.reddit.com/r/acturnips/new/ if the submission's author:

* (a) advertises a buying price over ``x`` bells. 

or

* (b) advertises a selling price ``x`` bells.

The bot also allows you to filter submissions by number of minutes since posted.

# requirements

the imported libraries in ``setup.py``, a client id, client secret, and username/password from reddit: https://github.com/reddit-archive/reddit/wiki/OAuth2

