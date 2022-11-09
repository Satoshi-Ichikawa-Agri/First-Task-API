""" 要件
1. 猫、犬、狐の画像が表示される以下のAPIを利用して、以下のgifのように選択した動物の画像が表示されるようにしてください。
"""
import requests
from flask import Flask
from flask import render_template
from PIL import Image


app = Flask(__name__, static_folder="FirstWeekTasks\First-Task-API\images\dog.png")


@app.route("/")
def index():
    return render_template("Index.html")


def main():
    url = "https://dog.ceo/api/breeds/image/random"
    request = requests.get(url)
    # print(request) → Response[200]
    image_data = request.json()
    image_url = image_data["message"]
    download_image(url=image_url, file_path="images/dog.png")


def download_image(url, file_path):
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(file_path, "wb") as f:
            f.write(request.content)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
