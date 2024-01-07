from flask import Flask, render_template

from page_analyzer.cfg import SECRET_KEY

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/")
def start_page():
    return render_template('index.html')


@app.post("/urls")
def verify_url():
    return '<h1>Method not allowed!<h1>', 405
