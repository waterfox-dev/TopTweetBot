import requests
import json

from twitter_api import *
from text_to_image import *
from cloud_support import *

with open("appInstagramConfig.json", 'r') as read_file:
    read_file = json.load(read_file)


def postInstagramQuote(image_link, caption):

    post_url = 'https://graph.facebook.com/v10.0/{}/media'.format(
        read_file['instagram']['instagram_business_account']['id'])

    payload = {
        'image_url': image_link,
        'caption': caption,
        'access_token': read_file['access_token']
    }

    r = requests.post(post_url, data=payload)    
    result = json.loads(r.text)

    if 'id' in result:
        creation_id = result['id']

        second_url = 'https://graph.facebook.com/v10.0/{}/media_publish'.format(
            read_file['instagram']['instagram_business_account']['id'])

        second_payload = {
            'creation_id': creation_id,
            'access_token': read_file['access_token']
        }

        r = requests.post(second_url, data=second_payload)

    else :
        print(result)
        print("An error was occured during the sending of image please, check the log")


top_tweet = get_tweet()

try :
    text_to_image(transform(top_tweet.text,top_tweet.user.name),top_tweet.entities['media'][0]['media_url'])

except :
    text_to_image(transform(top_tweet.full_text,top_tweet.user.name))

a = upload("text_to_image")

postInstagramQuote(a, "Test")