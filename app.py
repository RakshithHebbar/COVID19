#!/usr/bin/env python3
# This modules contains all the routes for the functioning
# of the application.

from flask import Flask, render_template, request, redirect, jsonify, url_for
import json
import requests



app = Flask(__name__)

@app.route('/')
def home():
    """Route to the homepage."""
    uri = "https://coronavirus-19-api.herokuapp.com/all"
    #uri = "https://coronavirus-tracker-api.herokuapp.com/v2/latest"
    try:
        uResponse = requests.get(uri)
    except:
        return False
    Jresponse = uResponse.text
    data = json.loads(Jresponse)
    uri = "https://coronavirus-19-api.herokuapp.com/countries"
    try:
        uResponse = requests.get(uri)
    except:
        return False
    Jresponse = uResponse.text
    countrydata = json.loads(Jresponse)

    return render_template(
        'index.html', data=data, countrydata=countrydata)

@app.route('/view_country/<country>/')
def view_country(country):
    uri = "https://coronavirus-19-api.herokuapp.com/countries"
    try:
        uResponse = requests.get(uri)
    except:
        return False
    Jresponse = uResponse.text
    inputdata = json.loads(Jresponse)
    inputcountry = [x for x in inputdata if x['country'] == country]
    print('countrydata', inputcountry[0])
    return render_template(
        'view-country.html', inputcountry=inputcountry[0])
    


if __name__ == "__main__":
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.run(host="0.0.0.0", port=8000, debug=True)
