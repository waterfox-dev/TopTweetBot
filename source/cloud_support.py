import cloudinary.uploader
import json
import os

with open("config/cloudinaryConfig.json", "r") as cc :
    cc = json.load(cc)

cloudinary.config( 
  cloud_name = cc['cloud_name'], 
  api_key = cc['api_key'], 
  api_secret = cc['api_secret'] 
)

def upload(file_name, public_id = "TopTweetOfDay") :
    a = cloudinary.uploader.upload(f"pictures/{file_name}.png", 
        public_id = public_id)
    return a['secure_url']

def delete_from_cloud():
    cloudinary.uploader.destroy("TopTweetOfDay")