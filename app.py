import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Tyler Teichmann in 3308'

@app.route("/db_test")
def testing():
    conn = psycopg2.connect("postgresql://db_hello_world_user:T5nfjWI8ihyWIjN8Gi0T4wkii4xdniEg@dpg-csgni788fa8c7390lbeg-a/db_hello_world")
    conn.close()
    return "Database Connection Successful"