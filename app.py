from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "http://forgifs.com/gallery/d/293417-3/Knock-knock-cats.gif?",
    "http://forgifs.com/gallery/d/201455-3/Cat-hug.gif?",
    "http://forgifs.com/gallery/d/296246-2/Cat-attacks-ballooncat.gif?",
    "http://forgifs.com/gallery/d/298258-2/Cat-fishing-ice-force-field.gif?",
    "http://forgifs.com/gallery/d/296892-3/Cat-VS-trash-can.gif?",
    "http://forgifs.com/gallery/d/297214-2/Jerk-cat-toys-with-vase.gif?",
    "http://forgifs.com/gallery/d/298536-2/Lazy-cat-paw-water.gif?",
    "http://forgifs.com/gallery/d/299244-2/Cat-rolls-off-edge-clings.gif?",
    "http://forgifs.com/gallery/d/300763-2/Mom-falls-kittens-scatter.gif?"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

