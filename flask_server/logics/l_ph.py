def l_ph(connection_pred_db,connection_sensor_db):
    #define defaul variables (given by the owner) ******* consider about min and max while editing
    ph_min=25
    ph_max=30
    time_one_unit = 10/2.5  #10/2.5*60 To reduce the value by 2.5c, 10 minutes the relay switch should be on    
    
    #get last row value of table ph from predicted data db    
    cursor_pred_db = connection_pred_db.cursor()
    cursor_pred_db.execute("select value from ph ORDER BY id DESC LIMIT 1")
    myresult_p = cursor_pred_db.fetchall()
    p_ph = float(myresult_p[0][0])

    #logics for ph
    #check if value is less than minimum value or greater than maximum value
    if p_ph<ph_min or p_ph>ph_max:
        #response for activate ph

        #get sensor data
        cursor_sensor_db = connection_sensor_db.cursor()
        cursor_sensor_db.execute("select value from ph ORDER BY id DESC LIMIT 1")
        myresult_s = cursor_sensor_db.fetchall()
        sensor_ph = float(myresult_s[0][0])

        #response for control ph
        resp=[{
                "out_func_name":"ph_cont",
                "is_on":True,
                "time_on_s":round((time_one_unit)*abs(sensor_ph-p_ph))
            }
        ]
        
    
    else:
        #response for nothing change algae
        resp=[{
                "out_func_name":"ph_cont",
                "is_on":False,
                "time_on_s":None
            }

            ]
    return resp
