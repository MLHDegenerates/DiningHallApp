from app import app, data
from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'friend'}
    drinks = [
        {
            'name': 'cola',
            'colour': 'red'
        },
        {
            'name': 'drank',
            'colour': 'purple'
        },
        {
            'name': 'Pop',
            'colour': 'Orange'
        }
    ]
    return render_template('index.html', title='Home', user=user, drinks=drinks)


@app.route('/dom')
def dom():
    myMap = Map(
        identifier="sndmap",
        lat=data.lat,
        lng=data.lng,
        markers=data.halls,
        zoom=15,
        style="height:600px;width:600px;margin:0;"
    )
    return render_template('dom.html', mymap=myMap)


@app.route('/ben')
def ben():
    return render_template('Ben.html')


@app.route('/val')
def val():
    return render_template('Val.html')


@app.route('/haadia')
def haadia():
    return render_template('Haadia.html')


@app.route('/Leonard')
def Leonard():
    return render_template("Leonard.html")

@app.route('/BanRight')
def BanRight():
    return render_template("BanRight.html")