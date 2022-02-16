from flask import Flask
from utilities.db_connection import db_connection

app = Flask(__name__)

@app.route("/")
def main_program():
	
	
	test = db_connection()
	return "<p>Hello, World!</p>"
