from flask import Flask, render_template, jsonify

app = Flask(__name__,static_url_path='',static_folder='templates')

@app.route('/')
def home():
    return render_template("home.html")