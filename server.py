import os

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("center.html")

@app.route("/info")
def press_info():
    return render_template("informs.html")

@app.route("/price")
def price_list():
    return render_template("price.html")


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)