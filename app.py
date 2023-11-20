# app.py  Build a Flask app with static HTML pages and navigate between them
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/office')
def office():
    return render_template('office.html')

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 8070)