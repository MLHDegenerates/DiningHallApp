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
    print("what is happening")
    return render_template('index.html', title='Home', user=user, drinks=drinks)
