from camera import capture
from flask import Flask
from notif import send_notif
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
@cross_origin()    
def home():
    result = capture()
    if result == 0:
        return "scissors"
    elif result == 1:
        return "syringe"
    elif result == 2:
        return "bottle"
    elif result == 3:
        return "bandage"
    else:
        return "Invalid value returned by capture()"
    

@app.route("/notify")
@cross_origin()    
def notify():
    if(send_notif()):
        return "Notification sent"
    else:
        return "Failed to send notification. Please retry"
    
if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)


# 0 - scissors
# 1 - syringe
# 2 - bottle  
# 3 - bandage