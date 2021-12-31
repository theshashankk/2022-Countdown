from flask import Flask, render_template
from config import NAME,IMAGE, SHORT_BIO, ABOUT, GITHUB, FACEBOOK, INSTAGRAM

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", name=NAME, image=IMAGE, bio=SHORT_BIO, about=ABOUT, git=GITHUB, fb=FACEBOOK, ig=INSTAGRAM)



if __name__ == "__main__":
    app.run(debug=False)
