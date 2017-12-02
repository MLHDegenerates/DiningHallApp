from app import app, data
from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/map')
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


@app.route('/leonard')
def leonard():
    return render_template("leonard.html")


@app.route('/banrigh')
def banrigh():
    return render_template("banrigh.html")


@app.route('/jeanroyce')
def jeanroyce():
    return render_template("jeanroyce.html")
