from flask import Flask
from utilities.db_connection_sensor_db import db_connection_sensor
from utilities.db_connection_pred_db import db_connection_pred
from logics.l_temp import l_temp
from logics.l_hum import l_hum
from logics.l_light_ins import l_light_ins
from logics.l_ph import l_ph
from logics.l_algae import l_algae
from logics.l_fish_feed import l_fish_feed

from collections import ChainMap



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
			ls_ph_res = l_ph(connection_pred_db,connection_sensor_db)
			ls_algae_res = l_algae(connection_pred_db,connection_sensor_db)
			ls_fish_feed_res = l_fish_feed(connection_pred_db,connection_sensor_db)

			response_ls = ls_temp_res+ls_hum_res+ls_light_ins_res+ls_ph_res+ls_algae_res+ls_fish_feed_res

			#convert ls to dict
			response_dict = {}
			for item in response_ls:
   				name = item['out_func_name']
   				response_dict[name] = item
			

			#print(response_dict)
			return response_dict
		except:
			print('unable to execute logics... check internal logics')
	except:
		print("unable to connect databases... check your db connection")	
	return 500 #internal server error


# app.py
if __name__ == "__main__":
    app.run(debug=True)