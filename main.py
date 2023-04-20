import requests
import sys
from dotenv import load_dotenv
import openalpr
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def process():
    image_names = []
    plate_info = []
    for uploaded_file in request.files.getlist('image'):
        filename = secure_filename(uploaded_file.filename)
        uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        file_image = {"image": open(os.path.join(app.config['UPLOAD_FOLDER'], filename), "rb")}
        data = openalpr.make_requests(file_image)

        image_names.append(filename)
        plate_info.append(openalpr.analyse_results(data.json()))

    return render_template("index.html", list_images=image_names, plate_info=plate_info)


if __name__ == '__main__':
    app.run(debug=True)
