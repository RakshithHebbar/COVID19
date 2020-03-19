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
    if inputcountry[0]["country"] == 'India':
        inputcountry[0]["helpline"] = [{"state":"Andhra Pradesh","phone":"0866-2410978"},{"state":"Arunachal Pradessh","phone":"9436055743"},{"state":"Assam","phone":"6913347770"},{"state":"Bihar","phone":"104"},{"state":"Chhattisgarh","phone":"104"},{"state":"Goa","phone":"104"},{"state":"Gujarat","phone":"104"},{"state":"Haryana","phone":"8558893911"}
        ,{"state":"Himachal Pradesh","phone":"104"},{"state":"Jharkhand","phone":"104"}
        ,{"state":"Karnataka","phone":"104"},{"state":"Kerala","phone":"0471-2552056"},{"state":"Madhya Pradesh","phone":"0755-2527177"},{"state":"Maharashtra","phone":"020-26127394"},{"state":"Manipur","phone":"3852411668"},{"state":"Meghalaya","phone":"108"},{"state":"Mizoram","phone":"102"}
        ,{"state":"Nagaland","phone":"7005539653"},{"state":"Odisha","phone":"9439994859"}
        ,{"state":"Punjab","phone":"104"},{"state":"Rajasthan","phone":"0141-2225624"},{"state":"Sikkim","phone":"104"},{"state":"Tamil Nadu","phone":"044-29510500"},{"state":"Telangana","phone":"104"},{"state":"Tripura","phone":"0381-2315879"},{"state":"Uttarakhand","phone":"104"},{"state":"Uttar Pradesh","phone":"18001805145"},{"state":"West Bengal","phone":"1800313444222, 03323412600"},{"state":"Andaman and Nicobar Islands","phone":"03192-232102"},{"state":"Chandigarh","phone":"9779558282"},{"state":"Dadra and Nagar Haveli and Daman & Diu","phone":"104"},{"state":"Delhi","phone":"011-22307145"},{"state":"Jammu & Kashmir","phone":"01912520982, 0194-2440283"},{"state":"Ladakh","phone":"01982256462"},{"state":"Lakshadweep","phone":"104"},{"state":"Puducherry","phone":"104"}]

    print('countrydata', inputcountry[0])
    return render_template(
        'view-country.html', inputcountry=inputcountry[0])
    


if __name__ == "__main__":
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.run(host="0.0.0.0", port=8000, debug=True)
