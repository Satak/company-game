import json
from flask import Flask, render_template
app = Flask(__name__)

COMPANY_DATA_FILE = '../data/company.json'
CIVIL_DATA_FILE = '../data/civil.json'


def get_json_data(file):
    with open(file, encoding='utf-8') as json_file:
        return json.load(json_file)


@app.route('/')
def index_route():
    return {'message': 'index'}


@app.route('/companies')
def companies_route():
    return render_template('cards.html', companies=get_json_data(COMPANY_DATA_FILE))


@app.route('/civil')
def civil_route():
    return render_template('cards.html', companies=get_json_data(CIVIL_DATA_FILE))
