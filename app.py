""" 要件
1. 猫、犬、狐の画像が表示される以下のAPIを利用して、以下のgifのように選択した動物の画像が表示されるようにしてください。
"""
from flask import Flask
from flask import render_template
from flask import request


# Flaskオブジェクトを作成
app = Flask(__name__)


@app.route("/")
def Index():
    return render_template("Index.html")


@app.route("/selectAnimal", methods=["POST"])
def selectAnimal():
    img = Image.open(file)
    img.save("images/test.png")
    img.show()


# Conduct application
if __name__ == "__main__":
    app.run(debug=True)
