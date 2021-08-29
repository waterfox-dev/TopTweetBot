import json

def read_today():
    with open("API/todayPost.json", 'r') as reading_today :
        return json.load(reading_today)