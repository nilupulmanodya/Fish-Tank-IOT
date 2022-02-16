from flask import Flask
from utilities.db_connection_sensor_db import db_connection_sensor
from utilities.db_connection_pred_db import db_connection_pred
from logics.l_temp import l_temp
from logics.l_hum import l_hum
from logics.l_light_ins import l_light_ins


app = Flask(__name__)


@app.route("/")
def main_program():
	
	#trying to connect dbs
	try:
		connection_pred_db = db_connection_pred()
		connection_sensor_db = db_connection_sensor()

		try:

			ls_temp_res=l_temp(connection_pred_db,connection_sensor_db)
			ls_hum_res=l_hum(connection_pred_db,connection_sensor_db)
			ls_light_ins_res=l_light_ins(connection_pred_db,connection_sensor_db)

			print(ls_light_ins_res)
		except:
			print('unable to execute logics... check intenal logics')
	except:
		print("unable to connect databases... check your db connection")
		return 0
	
	return "<p>Hello, World!</p>"


# app.py
if __name__ == "__main__":
    app.run(debug=True)