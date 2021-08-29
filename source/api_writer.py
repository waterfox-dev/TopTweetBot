import json

def write_today(id, date, image_link, author, text) :

    with open('API/todayPost.json', 'r') as today_post_reader :
        today_post_reader = json.load(today_post_reader)
        
        today_post_reader['id']        = id 
        today_post_reader['date']      = date
        today_post_reader['imageLink'] = image_link
        today_post_reader['tweetInfo']['author']    = author
        today_post_reader['tweetInfo']['text']      = text

        with open('API/todayPost.json', 'w') as today_post_writer :
            json.dump(today_post_reader, today_post_writer)