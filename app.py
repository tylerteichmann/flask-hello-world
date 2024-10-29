from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Tyler Teichmann in 3308'
