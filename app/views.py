from flask import render_template
from flask_googlemaps import Map
from app import app


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
    return render_template('dom.html')


@app.route('/ben')
def ben():
    return render_template('Ben.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/')
def mapview():
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )
    return render_template('mymap.html', mymap=mymap)