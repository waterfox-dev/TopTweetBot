import json
from cloud_support import *

def write_today(id, date, image_link, author, text) :

    with open('API/todayPost.json', 'r') as today_post_reader :
        today_post_reader = json.load(today_post_reader)
        
        today_post_reader['id']        = id 
        today_post_reader['date']      = date
        today_post_reader['imageLink'] = image_link
        today_post_reader['author']    = author
        today_post_reader['text']      = text

        with open('API/todayPost.json', 'w') as today_post_writer :
            json.dump(today_post_reader, today_post_writer)

def write_post(id, date, author, text) :
    
    image_link = upload("text_to_image", id)

    with open('API/data.json', 'r') as data_reader :
        data_reader = json.load(data_reader)
        data_reader[id] = {}
        
    with open ('API/data.json', 'w') as data_writer :
        json.dump(data_reader, data_writer)
    
    with open('API/data.json', 'r') as data_reader :
        id = str(id)
        data_reader = json.load(data_reader)
        data_reader[id]['date'] = date
        data_reader[id]['imageLink'] = image_link
        data_reader[id]['author'] = author
        data_reader[id]['text'] = text

    with open ('API/data.json', 'w') as data_writer :
        json.dump(data_reader, data_writer)

