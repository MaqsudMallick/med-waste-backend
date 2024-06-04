import os
import requests
from PIL import Image
from io import BytesIO
import random
import string
from model import get_class

cam_address = "http://192.168.43.1:8080/"
url = f"{cam_address}/shot.jpg"
save_dir = r'C:\Users\HP\Downloads\CaptureImage'  # Use raw string to handle backslashes

def generate_random_filename(extension="jpg"):
    """Generates a random filename with the given extension."""
    filename = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return f"{filename}.{extension}"

def capture():
    # Ensure the directory exists
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Fetching data from the URL
    img_resp = requests.get(url)
    img = Image.open(BytesIO(img_resp.content)).convert('RGB')

    # Save the image with a random name
    filename = generate_random_filename()
    filepath = os.path.join(save_dir, filename)
    img.save(filepath)

    # Proceed with further processing
    return get_class(img)

# capture()
