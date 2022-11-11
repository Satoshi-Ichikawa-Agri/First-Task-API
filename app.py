""" 要件
1. 猫、犬、狐の画像が表示される以下のAPIを利用して、以下のgifのように選択した動物の画像が表示されるようにしてください。
"""
import json
import requests
import secrets
from flask import Flask
from flask import render_template
from flask import request


# Flaskオブジェクトの生成
app = Flask(__name__)


# セッション情報を暗号化するためのキー設定
app.secret_key = secrets.token_urlsafe(32)


# GET index
@app.route("/")
def index():
    return render_template("index.html")


# POST Animal
@app.route("/animal", methods=["POST"])
def animal():
    if request.form["selectAnimal"] == "cat":
        res = requests.get("https://api.thecatapi.com/v1/images/search")
        outfile = json.loads(res.text)[0]["url"]
    elif request.form["selectAnimal"] == "dog":
        res = requests.get("https://dog.ceo/api/breeds/image/random")
        outfile = json.loads(res.text)["message"]
    else:
        res = requests.get("https://randomfox.ca/floof")
        outfile = json.loads(res.text)["image"]
    return render_template("animal.html", outfile=outfile)


if __name__ == "__main__":
    app.run(debug=True)
