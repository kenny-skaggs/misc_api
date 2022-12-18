from datetime import datetime

from flask import Flask


app = Flask(__name__)

@app.route('/today')
def get_today():
    return datetime.now().strftime('%b %-d, %Y')
