from app import app
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
        identifier="view-side",
        lat=37.4419,
        lng=-112.1419,
        markers=[(37.4419, -122.1419)]
    )
    sndmap = Map(
        identifier="sndmap",
        lat=37.4419,
        lng=-112.1419,
        markers=[
            {
                'icon': "http://maps.google.com/mapfiles/ms/icons/green-dot.png",
                'lat': 37.4419,
                'lng': -112.1419,
                'infobox': "<b>Hello World</b>"
            },
            {
                'icon': "http://maps.google.com/mapfiles/ms/icons/blue-dot.png",
                'lat': 37.4300,
                'lng': -112.1419,
                'infobox': "<b>Hello World from elsewhere</b>"
            }
        ]
    )
    return render_template('dom.html', mymap=myMap, sndmap=sndmap)


@app.route('/ben')
def ben():
    return render_template('Ben.html')
