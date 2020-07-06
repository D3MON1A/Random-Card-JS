"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db
from api.utils import generate_sitemap
import random

#from models import Person

api = Blueprint('api', __name__)


@api.route('/card', methods=['GET'])


# high_values = 

def get_random_card():
    suites = ['♡','♢','♤','♧']
    values = list(range(1,14))
    # your code here
    suite = random.choice(suites)
    value = str(random.choice(values))
    if value == "11":
        value = "J"
    elif value == "12":
        value = "Q"
    elif value == "13":
        value = "K"
    elif value == "14":
        value = "A"
    random_card = suite + str(value)

    response_body = {
        suite : value
    }

    return jsonify(response_body), 200