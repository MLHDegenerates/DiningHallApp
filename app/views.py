from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'friend'}
    drinks = [
        {
            'name':'cola',
            'colour':'red'
        },
        {
            'name':'drank',
            'colour':'purple'
        },
        {
            'name':'Fanta',
            'colour':'Orange'
        }
    ]
    return render_template('index.html', title='Home', user=user, drinks=drinks)


@app.route('/dom')
def dom():
    return render_template('dom.html')