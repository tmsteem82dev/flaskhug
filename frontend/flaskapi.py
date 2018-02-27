from flask import Flask, render_template, jsonify, request
import requests
import base64
from binascii import a2b_base64
import emailer


app = Flask(__name__,static_url_path='',static_folder='templates')

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/uploader', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']

        file = {"file": request.files['file'].stream}
        data = {"file_description": request.form["description"],
                "file_name": request.files['file'].filename}

        response = requests.post("http://localhost:8000/upload", files=file, data=data)
        return jsonify(response)

    return "BAD"

@app.route("/uploader/image", methods=["POST"])
def upload_image():
    if request.method == "POST":
        raw_img_data = request.form["image_data"]
        splitsies = raw_img_data.split(",")

        img_data = a2b_base64(splitsies[1])
        filename = "someimg.jpg"
        with open(filename,"wb") as f:
            f.write(img_data)
            f.close()

        return "OK"

# @app.route("/emailer/send",methods=["POST"])
# def email_message():
#     msg = ""
#     if request.method == "POST":
#         msg = request.data.decode('utf-8')
#         emailer.email_message("tmsteem82@gmail.com", msg)
#
#     return "OK"

@app.route("/emailer/send",methods=["POST"])
def email_message():
    if request.method == "POST":
        raw_img_data = request.form["image_data"]
        html_body = request.form["html_body"]
        img_id = request.form["img_id"]
        splitsies = raw_img_data.split(",")

        img_data = a2b_base64(splitsies[1])
        filename = "someimg.png"
        with open(filename,"wb") as f:
            f.write(img_data)
            f.close()

        emailer.email_attached_img("tmsteem82@gmail.com", html_body, filename, img_id)

    return "OK"

@app.route("/emailer/sendyag", methods=["POST"])
def email_yag():
    if request.method == "POST":
        raw_img_data = request.form["image_data"]

        emailer.yagmail_test("tmsteem82@gmail.com", "", raw_img_data)

    return "OK"


if __name__ == "__main__":
    app.run(debug=True)