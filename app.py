from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home():
    result = random.choice(["大吉", "中吉", "小吉", "吉", "凶"])
    return f"<h1>今日の運勢</h1><h2>{result}！</h2>"

if __name__ == "__main__":
    app.run()
