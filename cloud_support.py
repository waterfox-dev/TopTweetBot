import cloudinary.uploader
import json

with open("cloudinaryConfig.json", "r") as cc :
    cc = json.load(cc)

cloudinary.config( 
  cloud_name = cc['cloud_name'], 
  api_key = cc['api_key'], 
  api_secret = cc['api_secret'] 
)

def upload(file_name) :
    a = cloudinary.uploader.upload(f"pictures/{file_name}.png", 
        public_id = "TopTweetOfDay")
    
    return a['secure_url']