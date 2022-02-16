def l_hum(connection_pred_db,connection_sensor_db):
    #define defaul variables (given by the owner) ******* consider about min and max while editing
    hum_min=25
    hum_max=30
    time_one_unit = 10/2.5  #To reduce the value by 2.5c, 10 minutes the relay switch should be on    
    
    #get last row value of table humidity from predicted data db    
    cursor_pred_db = connection_pred_db.cursor()
    cursor_pred_db.execute("select value from Humidity ORDER BY id DESC LIMIT 1")
    myresult_p = cursor_pred_db.fetchall()
    p_hum = float(myresult_p[0][0])

    #logics for humidity
    #check if value is less than minimum value
    if p_hum<hum_min:

        #get sensor data
        cursor_sensor_db = connection_sensor_db.cursor()
        cursor_sensor_db.execute("select value from Humidity ORDER BY id DESC LIMIT 1")
        myresult_s = cursor_sensor_db.fetchall()
        sensor_hum = float(myresult_s[0][0])

        #response for decrease hum
        resp=[{
                "out_func_name":"hum_dec",
                "is_on":True,
                "time_on_s":round((time_one_unit)*(sensor_hum-p_hum))
            },
            {
                "out_func_name":"hum_inc",
                "is_on":False,
                "time_on_s":None
            }

        ]
        
    #check if value is greater than maximum value
    elif p_hum>hum_max:
        #get sensor data
        cursor_sensor_db = connection_sensor_db.cursor()
        cursor_sensor_db.execute("select value from Humidity ORDER BY id DESC LIMIT 1")
        myresult_s = cursor_sensor_db.fetchall()
        sensor_hum = float(myresult_s[0][0])

        #response for increase hum
        resp=[{
                "out_func_name":"hum_dec",
                "is_on":False,
                "time_on_s":None
            },
            {
                "out_func_name":"hum_inc",
                "is_on":True,
                "time_on_s":round((time_one_unit)*(p_hum-sensor_hum))
            }

        ]
    
    else:
        #response for nothing change hum
        resp=[{
                "out_func_name":"hum_inc",
                "is_on":False,
                "time_on_s":None
            },
            {
                "out_func_name":"hum_dec",
                "is_on":False,
                "time_on_s":None
            }

        ]
    return resp
