from instapy import InstaPy
import random
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

session = InstaPy(username=username,
                 password=password,
                 disable_image_load=True,
                 headless_browser=False)
session.login()

hashtags = [
    'motivation', 'fitness', 'inspiration', 'love', 'life', 'instagood', 'quotes', 'lifestyle', 'success',
     'motivationalquotes', 'workout', 'instagram', 'gym', 'goals', 'happy', 'believe', 'follow', 'mindset',
      'positivevibes', 'fitnessmotivation', 'fit', 'training', 'happiness', 'bhfyp', 'selflove', 'like',
       'health', 'entrepreneur', 'bodybuilding', 'bhfyp'
    ]

random.shuffle(hashtags)
my_hashtags = hashtags[:10]

#making sure the bot does not comment too much or look suspicious to the instagram algorithm
#Yet to work on the amount of server calls
session.set_quota_supervisor(enabled=True, sleep_after=["comments_d, follows_d"], sleepyhead=True, stochastic_flow=True,
                            peak_comments_daily= 100,
                            peak_comments_hourly=30, 
                            peak_likes_daily=200, 
                            peak_likes_hourly=30,
                            peak_follows_daily=None,
                            peak_follows_hourly=30,
                            peak_server_calls_daily=4700)

#To make sure the bot does not interact with accounts that have more than 5000 followers
session.set_relationship_bounds(enabled=True, max_followers= 5000)

# This is used to skip users with certain condition
session.set_skip_users(skip_private=True, private_percentage=80,)

#allows the bot to interract with people, used when bot follows likers or commentors of
# a post by setting interact parameter to true (code below this one)
session.set_user_interact(amount=2, percentage=50, randomize=True, media=None)

# follow the people that liked photos of given list of users
session.follow_likers(usernames=[username],
                    photos_grab_amount=5,
                    follow_likers_per_photo=3,
                    randomize=True,
                    sleep_delay=600,
                    interact=True)


# follow the people that commented on photos of given list of users
session.follow_commenters(usernames=[username],
                        amount=5,
                        daysold=100,
                        max_pic=5,
                        sleep_delay=600,
                        interact=True)


#The comments that the bot will be writing
session.set_comments([       u':fire: :fire: :fire: awsome stuff here!'
                             u'What an amazing shot! :fire: What do '
                             u'you think of my recent shot?',
                             u'What an amazing shot! :fire: I think '
                             u'you might also like mine. :wink:',
                             u'Wonderful!! :fire: Would be awesome if '
                             u'you would checkout my photos as well!',
                             u'Wonderful!! :fire: I would be honored '
                             u'if you would checkout my images and tell me '
                             u'what you think. :wink:',
                             u'This is awesome!! :fire: Any feedback '
                             u'for my photos? :wink:',
                             u'This is awesome!! :fire:  maybe you '
                             u'like my photos, too? :wink:',
                             u'I really like the way you captured this :fire:. I '
                             u'bet you like my photos, too :wink:',
                             u'I really like the way you captured this. If '
                             u'you have time, check out my photos, too. I '
                             u'bet you will like them. :fire: :wink:',
                             u'Great capture!! :fire: Any feedback for my '
                             u'recent shot? :fire:',
                             u'Great capture!! :fire: :thumbsup: What do '
                             u'you think of my recent photo?'],
                         media='Photo')

#The action that the bot performs and the percentages

session.set_dont_like(['sad', 'rain', 'depression', 'nsfw', 'nude'])
session.set_do_like(True, percentage=70)
session.set_do_follow(True, percentage=50, times=1)
session.set_do_comment(True, percentage=50)

#How the bot will watch stories
session.story_by_tags(my_hashtags[:3])


# Allows the bot to watch instagram stories 
session.set_do_story(enabled=True, percentage=80, simulate=False)


#The tags that the bot will be using to find users
session.like_by_tags(my_hashtags, amount=10)




# """ Joining Engagement Pods...
# """
# session.join_pods(topic='motivation', engagement_mode='no_comments')

session.end()