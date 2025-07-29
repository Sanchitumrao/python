#create a virtual environment
#pip install flask (install flask in virtual environment)
#import flask
from flask import Flask 

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Home Page!"

#start the server
app.run(debug=True)