from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://media.tenor.com/zZ1i8J3C2RUAAAAM/hello-robert-e-fuller.gif",
    "https://media.tenor.com/1y8rq5FE6OEAAAAM/yawning-robert-e-fuller.gif",
    "https://media.tenor.com/ohykMcgIpk8AAAAM/badgers-badgertime.gif",
    "https://media.tenor.com/KYE8V6nrzzYAAAAM/itchy-robert-e-fuller.gif",
    "https://media.tenor.com/YcZbpukPl34AAAAM/honey-badger-dance.gif"
]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
