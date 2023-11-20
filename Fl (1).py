from flask import Flask, request
app = Flask(__name__)


@app.route('/greet')
def greeting():
    return f"Hello, World!"

if __name__ == '__main__':
    app.run(host="0.0.0.0")

