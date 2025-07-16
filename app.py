from flask import Flask, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Date & Time API!"})

@app.route('/datetime')
def get_datetime():
    tz = pytz.timezone("Asia/Kolkata")
    now = datetime.now(tz)
    return jsonify({
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "timezone": str(tz)
    })

if __name__ == '__main__':
    app.run(debug=True)

