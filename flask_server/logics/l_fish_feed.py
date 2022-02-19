def l_fish_feed(connection_pred_db,connection_sensor_db):
    #define defaul variables (given by the owner) ******* consider about min and max while editing
    time_one_unit = 1  #5/5*60 If the value given is 5, the relay switch should be activated for 5 minutes.

    
    #get last row value of table FishFeeder from predicted data db    
    cursor_pred_db = connection_pred_db.cursor()
    cursor_pred_db.execute("select value from FishFeeder ORDER BY id DESC LIMIT 1")
    myresult_p = cursor_pred_db.fetchall()
    p_fish_feed = float(myresult_p[0][0])


    #generate response based on predicion db fish feeder value
    if p_fish_feed == 0:
        resp=[{
                    "out_func_name":"fish_feed_cont",
                    "is_on":False,
                    "time_on_s":None
                }
            ]
    else:

        resp=[{
                    "out_func_name":"fish_feed_cont",
                    "is_on":True,
                    "time_on_s":round((time_one_unit)*p_fish_feed)
                }
            ]

    return resp
