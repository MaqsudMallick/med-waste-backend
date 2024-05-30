import requests
from PIL import Image
from io import BytesIO
from model import get_class

cam_address = "ENTER_YOUR_CAM_ADDRESS"
url = f"{cam_address}/shot.jpg"


def capture():
# Fetching data from the URL
    img_resp = requests.get(url)
    img = Image.open(BytesIO(img_resp.content)).convert('RGB')

    return get_class(img)

# capture()
