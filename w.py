import requests
import json
#Pillow is used to write on a given image
from PIL import Image, ImageFont, ImageDraw
from datetime import date

api_key = "872f60095db63bc271856588336f0477"
position = [300,430,555,690,825]

uk_list = ["London", "Bristol", "Birmingham", "Manchestor", "Edinburgh"]
india_list = ["Jaipur", "Delhi", "Mumbai", "Kolkata", "Chennai"]
us_list = ["Chicago", "New York", "Los Angeles", "Miami", "Seattle"]
country_list = [uk_list, india_list, us_list]

#selecting first list in country list
for country in country_list:
    image = Image.open("post.png")
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('Inter-Medium.ttf', size=50)
    title = "Latest Weather Forecast"
    color = 'rgb(255,255,255)'
    (x,y) = (55,50)
    draw.text((x,y), title, color, font=font)

    font = ImageFont.truetype('Inter-Medium.ttf', size=50)
    title = date.today().strftime("%A - %B %d, %Y")
    color = 'rgb(255,255,255)'
    (x,y) = (55,145)
    draw.text((x,y), title, color, font=font)


    index = 0
    #selecting first city in the selected country list
    for city in country:
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=872f60095db63bc271856588336f0477&units=metric".format(city, api_key)
        response = requests.get(url)
        data = json.loads(response.text)
        
        font = ImageFont.truetype('Inter-Medium.ttf', size=50)
        color = 'rgb(0,0,0)'
        (x,y) = (135,position[index])
        draw.text((x,y), city, color, font=font)

        font = ImageFont.truetype('Inter-Medium.ttf', size=50)
        title = str(data['main']['temp']) + "\u00b0"
        color = 'rgb(255,255,255)'
        (x,y) = (600,position[index])
        draw.text((x,y), title, color, font=font)

        font = ImageFont.truetype('Inter-Medium.ttf', size=50)
        title = str(data['main']['humidity']) + "%"
        color = 'rgb(255,255,255)'
        (x,y) = (810,position[index])
        draw.text((x,y), title, color, font=font)

        index += 1

    image.save(str(date.today()) + country[0] + ".png") #to png
    image_pdf = image.convert('RGB')
    image_pdf.save(str(date.today()) + country[0] + ".pdf") #to pdf

