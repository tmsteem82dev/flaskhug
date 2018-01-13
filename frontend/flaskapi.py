from flask import Flask, render_template, jsonify, request
import requests
app = Flask(__name__,static_url_path='',static_folder='templates')

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/uploader', methods=['GET','POST'])
def upload_file():
    print("balls")
    if request.method == 'POST':
        f = request.files['file']

        file = {"file": request.files['file'].stream}
        data = {"file_description": request.form["description"],
                "file_name": request.files['file'].filename}

        response = requests.post("http://localhost:8000/upload",files=file,data=data)
        return jsonify(response)

    return "BAD"


if __name__ == "__main__":
    app.run(debug=True)