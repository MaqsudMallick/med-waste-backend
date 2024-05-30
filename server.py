from flask import Flask
from camera import capture
app = Flask(__name__)

@app.route("/")
def home():
    return f'{capture()}'


# 0 - scissors
# 1 - syringe
# 2 - bottle  
# 3 - bandage