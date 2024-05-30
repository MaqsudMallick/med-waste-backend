import requests
from PIL import Image
from io import BytesIO
from model import get_class
url = "http://192.168.0.152:8080/shot.jpg"


def capture():
# Fetching data from the URL
    img_resp = requests.get(url)
    img = Image.open(BytesIO(img_resp.content)).convert('RGB')

    return get_class(img)

# capture()