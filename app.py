# from flask import Flask
# app = Flask(__name__)

# #Index route
# @app.route('/')
# def index():
#     return "Hellooooo"

# #pets index route
# @app.route('/pets')
# def pets():
#     return "This is the Pet Page"    

from petfax import create_app

app = create_app()