import os

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("center.html")

@app.route("/info")
def press_info():
    return render_template("informs.html")

@app.route("/price", methods=["GET"])
def price_list():
    return render_template("price.html")

@app.route("/price", methods=["POST"])
def trace_init():
    try:
        date = request.form.get("date")
        surname = request.form.get("surname")
        if not date or not surname:
            print("Введены не все поля!")
            return render_template("center.html")
        else:
            print(surname, date)
            return render_template("price.html")
    except Exception:
        print("error")


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)