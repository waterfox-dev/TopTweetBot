import json
from logging import exception

from requests.api import get

class TTBError(Exception) :
    pass

def read_today():
    with open("API/todayPost.json", 'r') as reading_today :
        return json.load(reading_today)

def get_by_id(id) :
    with open("API/data.json", 'r') as reading_data :
        reading_data = json.load(reading_data)

        for keys in reading_data :
            if keys == str(id) :
                return reading_data[keys]
            else :
                raise TTBError("ID not found")

def get_by_date(date) :
    with open("API/data.json", 'r') as reading_data :
        reading_data = json.load(reading_data)

        for keys in reading_data :            
            if reading_data[keys]['date'] == date :
                return reading_data[keys]
            else :
                raise TTBError("Date not found")

def search_content(search_str) :
    with open("API/data.json", 'r') as reading_data :
        reading_data = json.load(reading_data)

        for keys in reading_data :
            if search_str in reading_data[keys]['text'] :
                return reading_data[keys]
            else :
                raise TTBError("This research return nothing, try an another element")
