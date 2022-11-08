""" 要件
1. 猫、犬、狐の画像が表示される以下のAPIを利用して、以下のgifのように選択した動物の画像が表示されるようにしてください。
"""
import io
import json
import requests
from flask import Flask
from flask import render_template
from PIL import Image


# Flaskオブジェクトを作成
app = Flask(__name__)


# GET Index
@app.route("/")
def index():
    return render_template("Index.html")


@app.route("/Animal", methods=["POST"])
def select_animal():
    return render_template("Animal.html")


def image():
    url = "https://dog.ceo/api/breeds/image/random"

    # (1)APIを実行
    responce = requests.get(url)

    # (2) 返ってきたJSONを処理
    jsonObj = responce.json()
    ImageUrl = jsonObj["message"]
    strImageURL = str(ImageUrl)

    # (3) 画像URLから画像表示
    file = io.BytesIO(requests.get(strImageURL).content)
    img = Image.open(file)
    img.save("images/out.png")
    img.show()


# Conduct application
if __name__ == "__main__":
    app.run(debug=True)
