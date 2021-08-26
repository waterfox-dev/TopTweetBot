from PIL import Image, ImageDraw, ImageFont
from requests.api import get
from twitter_api import get_tweet
from image_dl import toimage
from pilmoji import Pilmoji

def text_to_image(text, image = None) :

    if image != None :
        img = Image.new('RGB', (1500,1500), color  = (0,0,0))
        fnt =  ImageFont.truetype("Calibri Regular.ttf", 75)

        with Pilmoji(img) as pilmoji :
            pilmoji.text((175,175), text, font = fnt, fill = (255,255,255))
        
        shape = [(40, 40), (1460, 1460)]
        rectangle_draw = ImageDraw.Draw(img)
        rectangle_draw.rectangle(shape, outline="#1d9bf0", width=5)

        img.save("text_to_image.png")

        image_name = toimage(image)
        image_1 = Image.open("text_to_image.png")
        image_2 = Image.open(image_name)
        final_image = image_1.copy()
        final_image.paste(image_2, (((750-(int(image_2.size[0]/2))),750)))
        final_image.save("text_to_image.png")

    else :
        img = Image.new('RGB', (1500,1500), color  = (0,0,0))
        fnt =  ImageFont.truetype("Calibri Regular.ttf", 75)

        with Pilmoji(img) as pilmoji :
            pilmoji.text((200,300), text, font = fnt, fill = (230,230,230))
        
        shape = [(40, 40), (1460, 1460)]
        rectangle_draw = ImageDraw.Draw(img)
        rectangle_draw.rectangle(shape, outline="#1d9bf0", width=5)

        img.save("text_to_image.png")
    

def transform(text, author):
    text = list(text)
    lign_return = 0
    for element in range(len(text)) :
        if (element > 30 and element < 50 and text[element] == " " and lign_return == 0) :
            text[element] = '\n'
            lign_return += 1
        elif (element > 70 and element < 90 and text[element] == " "  and lign_return == 1) :
            text[element] = '\n'
            lign_return += 1
        elif (element > 90 and element < 120 and text[element] == " "  and lign_return == 2) :
            text[element] = '\n'
            lign_return += 1
        elif (element > 130 and element < 150 and text[element] == " "  and lign_return == 3) :
            text[element] = '\n'
            lign_return += 1
        elif (element > 170 and element < 190 and text[element] == " "  and lign_return == 4) :
            text[element] = '\n'
            lign_return += 1
        elif (element > 200 and element < 220 and text[element] == " "  and lign_return == 5) :
            text[element] = '\n'
            lign_return += 1
        elif (element > 230 and element < 260 and text[element] == " "  and lign_return == 6) :
            text[element] = '\n'
            lign_return += 1
        elif (element > 260 and element < 270 and text[element] == " "  and lign_return == 7) :
            text[element] = '\n'
            lign_return += 1
    new_text = ""
    for element in text :
        new_text += element
       
    link_indice = new_text.find("https://t.co/")
    new_text = new_text[:link_indice]
    new_text += f"\n \n \nAuthor : {author}"
    
    return new_text
