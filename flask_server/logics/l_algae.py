def l_algae(connection_pred_db,connection_sensor_db):
    #define defaul variables (given by the owner) ******* consider about min and max while editing
    algae_min=25
    algae_max=30
    time_one_unit = 1  #10/2.5*60 To reduce the value by 2.5c, 10 minutes the relay switch should be on    
    
    #get last row value of table  from predicted data db    
    cursor_pred_db = connection_pred_db.cursor()
    cursor_pred_db.execute("select value from turbidity ORDER BY id DESC LIMIT 1")
    myresult_p = cursor_pred_db.fetchall()
    p_algae = float(myresult_p[0][0])

    #logics for algae
    #check if value is less than minimum value or greater than maximum value
    if p_algae<algae_min or p_algae>algae_max:
        #response for activate algae

        #get sensor data
        cursor_sensor_db = connection_sensor_db.cursor()
        cursor_sensor_db.execute("select value from turbidity ORDER BY id DESC LIMIT 1")
        myresult_s = cursor_sensor_db.fetchall()
        sensor_algae = float(myresult_s[0][0])

        #response for control algae
        resp=[{
                "out_func_name":"alg_cont",
                "is_on":True,
                "time_on_s":round((time_one_unit)*abs(sensor_algae-p_algae))
            }
        ]
        
    
    else:
        #response for nothing change algae
        resp=[{
                "out_func_name":"alg_cont",
                "is_on":False,
                "time_on_s":None
            }

        ]
    return resp
