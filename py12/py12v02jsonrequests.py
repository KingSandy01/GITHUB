import json
import requests as rq
import string

# from matplotlib import pyplot as plt
# from matplotlib import image as mpimg

from PIL import Image

def get_data(url):
    try:
        return rq.get(url).text
    except Exception as e:
        print("Unable to load URL")

def load_json(data):
    if not data is None:
        j = json.loads(data)
        
        fname = j["results"][0]["name"]["first"]
        lname = j["results"][0]["name"]["last"]
        TPhoto = j["results"][0]["picture"]["large"]
        # # image = mpimg.imread(TPhoto)
        # # plt.imshow(image)
        # img = Image.open(str(TPhoto))
        return fname, lname, TPhoto
    
def main():
    url = "https://randomuser.me/api"

    values = load_json(get_data(url))

    if not values is None:
        print("First Name:", values[0])
        print("Last Name: ", values[1])
        print("Picture: ", values[2])

if __name__ == '__main__':
    main()
