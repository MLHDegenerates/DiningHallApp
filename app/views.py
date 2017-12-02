from app import app, data
from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/dom')
def map():
    myMap = Map(
        identifier="sndmap",
        lat=data.lat,
        lng=data.lng,
        markers=data.halls,
        zoom=15,
        style="height:600px;width:600px;margin:0;"
    )
    return render_template('map.html', mymap=myMap)

@app.route('/Leonard')
def Leonard():
    return render_template("leonard.html")

@app.route('/BanRigh')
def BanRigh():
    return render_template("banrigh.html")

@app.route('/JeanRoyce')
def JeanRoyce():
    return render_template("jeanroyce.html")