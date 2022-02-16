def l_temp(connection_pred_db,connection_sensor_db):
    #define defaul variables (given by the owner) ******* consider about min and max while editing
    temp_min=25
    temp_max=30
    time_one_unit = 10/2.5  #To reduce the value by 2.5c, 10 minutes the relay switch should be on    
    
    #get last row value of table temp from predicted data db    
    cursor_pred_db = connection_pred_db.cursor()
    cursor_pred_db.execute("select value from temperature ORDER BY id DESC LIMIT 1")
    myresult_p = cursor_pred_db.fetchall()
    p_temp = float(myresult_p[0][0])

    #logics for temp
    #check if value is less than minimum value
    if p_temp<temp_min:
        #response for increase temp

        #get sensor data
        cursor_sensor_db = connection_sensor_db.cursor()
        cursor_sensor_db.execute("select value from temperature ORDER BY id DESC LIMIT 1")
        myresult_s = cursor_sensor_db.fetchall()
        sensor_temp = float(myresult_s[0][0])

        #response for decrease temp
        resp=[{
                "out_func_name":"temp_dec",
                "is_on":True,
                "time_on_s":round((time_one_unit)*(sensor_temp-p_temp))
            },
            {
                "out_func_name":"temp_inc",
                "is_on":False,
                "time_on_s":None
            }

        ]
        
    #check if value is greater than maximum value
    elif p_temp>temp_max:
        #get sensor data
        cursor_sensor_db = connection_sensor_db.cursor()
        cursor_sensor_db.execute("select value from temperature ORDER BY id DESC LIMIT 1")
        myresult_s = cursor_sensor_db.fetchall()
        sensor_temp = float(myresult_s[0][0])

        #response for increase temp
        resp=[{
                "out_func_name":"temp_dec",
                "is_on":False,
                "time_on_s":None
            },
            {
                "out_func_name":"temp_inc",
                "is_on":True,
                "time_on_s":round((time_one_unit)*(p_temp-sensor_temp))
            }

        ]
    
    else:
        #response for nothing change temp
        resp=[{
                "out_func_name":"temp_inc",
                "is_on":False,
                "time_on_s":None
            },
            {
                "out_func_name":"temp_dec",
                "is_on":False,
                "time_on_s":None
            }

        ]
    return resp
