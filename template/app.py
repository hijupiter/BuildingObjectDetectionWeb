import os
from flask import Flask,render_template,flash,redirect,url_for,Markup
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY','secret string')

app.debug = True
@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('erros/404.html'),404