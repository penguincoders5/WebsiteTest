from flask import Flask, render_template, request
import json

from styler import STYLE

app = Flask(__name__)

colors = {
    'purple': '#7e6c6c',
    'darkpink': '#F87575',
    'pink': '#FFA9A3',
    'lightblue': '#B9E6FF',
    'blue': '#5C95FF',
    'green':'#49A078',
    'bg':'#4A4E69',
    'contain':'#22223b'

}



@app.route('/')
@app.route('/base')
def base():
    return render_template('base.html', s = STYLE('style.css'))


@app.route('/day', methods = ['GET', 'POST'])
def day():
    d = request.args["buttonId"]

    return render_template('day.html', day = d, s = STYLE('day.css'))
