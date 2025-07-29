#Creating and rendering html templates using Flask

from flask import Flask 

app = Flask(__name__)

#URL routing in flask
#Flask uses the @app.route() decorator to connect a URL to a Python function.
@app.route('/')
def home():
    return "Welcome to the Home Page!"

@app.route('/about')
def about():
    return "This is the about page"

#start the server
app.run(debug=True)