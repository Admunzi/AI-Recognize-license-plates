import os
import requests
import sys
from dotenv import load_dotenv

load_dotenv()

OPENALPR_URL = "https://api.openalpr.com/v2/recognize?recognize_vehicle=1&country=eu&secret_key=" + \
               os.getenv('API_KEY')
OPENALPR_PROCESSING_TIME = 'processing_time'
OPENALPR_RESULTS = 'results'
OPENALPR_CANDIDATES = 'candidates'
OPENALPR_VEHICLE = 'vehicle'
OPENALPR_MAKE = 'make'
OPENALPR_MAKE_MODEL = 'make_model'
OPENALPR_COLOR = 'color'


def analyse_results(results):
    candidate = results[OPENALPR_RESULTS][0][OPENALPR_CANDIDATES][0]
    make = results[OPENALPR_RESULTS][0][OPENALPR_VEHICLE][OPENALPR_MAKE][0]
    make_model = results[OPENALPR_RESULTS][0][OPENALPR_VEHICLE][OPENALPR_MAKE_MODEL][0]
    color = results[OPENALPR_RESULTS][0][OPENALPR_VEHICLE][OPENALPR_COLOR][0]

    json_plate = {
        'plate': candidate,
        'make': make,
        'make_model': make_model,
        'color': color
    }
    return json_plate


def make_requests(files):
    return requests.post(OPENALPR_URL, files=files)
