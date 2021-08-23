# Import dependencies
from flask import Flask

# Create an instance
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World, how are you?'

@app.route('/')
def how_are_you():
    return 'How are you?'