import mysql.connector
from mysql.connector import Error

def db_connection(db_username="userthut",db_pwd="thut"):
	connection = mysql.connector.connect(host='localhost',port='3306',
											 database='prediction_data',
											 user=db_username,
											 password=db_pwd)
	
	try:
		
		if connection.is_connected():
			db_Info = connection.get_server_info()
			print("Connected to MySQL Server version ", db_Info)
			cursor = connection.cursor()
			cursor.execute("select database();")
			record = cursor.fetchone()
			print("You're connected to database: ", record)

	except Error as e:
		print("Error while connecting to MySQL", e)
	finally:
		if connection.is_connected():
			cursor.close()
			connection.close()
			print("MySQL connection is closed")
