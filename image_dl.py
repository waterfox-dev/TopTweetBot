import requests # to get image from the web
import shutil

def toimage(url) :
    image_url = url
    filename = image_url.split("/")[-1]
    r = requests.get(image_url, stream = True)
    if r.status_code == 200:
        r.raw.decode_content = True
        
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            
        print('Image sucessfully Downloaded: ',filename)
        return filename
    else:
        print('Image Couldn\'t be retreived')   