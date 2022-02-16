import mysql.connector
from mysql.connector import Error
import utilities.auth.auths as auth


def db_connection_pred(db_username=auth.db_username,db_pwd=auth.db_pwd):
	connection = mysql.connector.connect(host='localhost',port='3306',
											 database='prediction_data',
											 user=db_username,
											 password=db_pwd)
	
	try:
		
		if connection.is_connected():
			db_Info = connection.get_server_info()
			print("Connected to MySQL Server version ", db_Info)
			#cursor = connection.cursor()
			#cursor.execute("select database();")
			#record = cursor.fetchone()
			#print("You're connected to database: ", record)
			return connection

	except Error as e:
		print("Error while connecting to MySQL", e)
"""	finally:
		if connection.is_connected():
			cursor.close()
			connection.close()
			print("MySQL connection is closed")
"""