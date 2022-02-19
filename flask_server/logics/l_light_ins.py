def l_light_ins(connection_pred_db,connection_sensor_db):
    #define defaul variables (given by the owner) ******* consider about min and max while editing
    light_ins_min=25
    light_ins_max=30
    time_one_unit = 1  #10/2.5*60 To reduce the value by 2.5c, 10 minutes the relay switch should be on    
    
    #get last row value of table light ins from predicted data db    
    cursor_pred_db = connection_pred_db.cursor()
    cursor_pred_db.execute("select value from LightIntensity ORDER BY id DESC LIMIT 1")
    myresult_p = cursor_pred_db.fetchall()
    p_light_ins = float(myresult_p[0][0])

    #logics for light ins
    #check if value is less than minimum value
    if p_light_ins<light_ins_min:
        

        #get sensor data
        cursor_sensor_db = connection_sensor_db.cursor()
        cursor_sensor_db.execute("select value from LightIntensity ORDER BY id DESC LIMIT 1")
        myresult_s = cursor_sensor_db.fetchall()
        sensor_light_ins = float(myresult_s[0][0])

        #response for decrease light ins
        resp=[{
                "out_func_name":"light_ins_dec",
                "is_on":True,
                "time_on_s":round((time_one_unit)*(sensor_light_ins-p_light_ins))
            },
            {
                "out_func_name":"light_ins_inc",
                "is_on":False,
                "time_on_s":None
            }

        ]
        
    #check if value is greater than maximum value
    elif p_light_ins>light_ins_max:
        #get sensor data
        cursor_sensor_db = connection_sensor_db.cursor()
        cursor_sensor_db.execute("select value from LightIntensity ORDER BY id DESC LIMIT 1")
        myresult_s = cursor_sensor_db.fetchall()
        sensor_light_ins = float(myresult_s[0][0])

        #response for increase light ins
        resp=[{
                "out_func_name":"light_ins_dec",
                "is_on":False,
                "time_on_s":None
            },
            {
                "out_func_name":"light_ins_inc",
                "is_on":True,
                "time_on_s":round((time_one_unit)*(p_light_ins-sensor_light_ins))
            }

        ]
    
    else:
        #response for nothing change light ins
        resp=[{
                "out_func_name":"light_ins_inc",
                "is_on":False,
                "time_on_s":None
            },
            {
                "out_func_name":"light_ins_dec",
                "is_on":False,
                "time_on_s":None
            }

        ]
    return resp
