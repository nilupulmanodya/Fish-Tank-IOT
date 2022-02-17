import machine
import uasyncio
import time


#settings
temp_inc = machine.Pin(5,machine.Pin.OUT)
temp_dec = machine.Pin(4,machine.Pin.OUT)
alg_cont = machine.Pin(2,machine.Pin.OUT)
ph_cont = machine.Pin(14,machine.Pin.OUT)
hum_inc = machine.Pin(12,machine.Pin.OUT)
hum_dec = machine.Pin(13,machine.Pin.OUT)
light_ins_dec = machine.Pin(16,machine.Pin.OUT)
light_ins_inc = machine.Pin(0,machine.Pin.OUT)
fish_feed_cont = machine.Pin(15,machine.Pin.OUT)

async def blink1(delay):
    
    print("time led1 on:",time.localtime())
    led1.on()        
    await uasyncio.sleep(delay)
    print("time led1 off:",time.localtime())
    led1.off()

async def temp_inc_s(delay):    
    temp_inc.on()        
    await uasyncio.sleep(delay)
    temp_inc.off()

async def temp_dec_s(delay):    
    temp_dec.on()        
    await uasyncio.sleep(delay)
    temp_dec.off()

async def alg_cont_s(delay):    
    alg_cont.on()        
    await uasyncio.sleep(delay)
    alg_cont.off()

async def ph_cont_s(delay):    
    ph_cont.on()        
    await uasyncio.sleep(delay)
    ph_cont.off()

async def hum_inc_s(delay):    
    hum_inc.on()        
    await uasyncio.sleep(delay)
    hum_inc.off()

async def hum_dec_s(delay):    
    hum_dec.on()        
    await uasyncio.sleep(delay)
    hum_dec.off()

async def light_ins_dec_s(delay):    
    light_ins_dec.on()        
    await uasyncio.sleep(delay)
    light_ins_dec.off()

async def light_ins_inc_s(delay):    
    light_ins_inc.on()        
    await uasyncio.sleep(delay)
    light_ins_inc.off()

async def fish_feed_cont_s(delay):    
    fish_feed_cont.on()        
    await uasyncio.sleep(delay)
    fish_feed_cont.off()


def connect_network():
    import network
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect("PROLINK_H5004NK_82FA6","vg2297788")
    station.isconnected()
    station.ifconfig()
    #print("success")
    return 0

def get_response():

	import urequests
	response = urequests.get('http://192.168.1.7:5000')
	parsed = response.json()
	#print(parsed)
	return parsed


#Coroutine entry point for asyncio program
async def main_controler(data):
    #print(data)
    if data['fish_feed_cont']['is_on']== True:
        #print('fish feed activated for (s):',data['fish_feed_cont']['time_on_s'])
        uasyncio.create_task(fish_feed_cont_s(data['fish_feed_cont']['time_on_s']))
    
    if data['ph_cont']['is_on']== True:        
        uasyncio.create_task(ph_cont_s(data['ph_cont']['time_on_s']))
        
    if data['temp_inc']['is_on']== True:    
        uasyncio.create_task(temp_inc_s(data['temp_inc']['time_on_s']))
        
    if data['temp_dec']['is_on']== True:    
        uasyncio.create_task(temp_dec_s(data['temp_dec']['time_on_s']))
        
    if data['light_ins_dec']['is_on']== True:        
        uasyncio.create_task(light_ins_dec_s(data['light_ins_dec']['time_on_s']))
        
    if data['alg_cont']['is_on']== True:        
        uasyncio.create_task(alg_cont_s(data['alg_cont']['time_on_s']))
        
    if data['hum_inc']['is_on']== True:    
        uasyncio.create_task(hum_inc_s(data['hum_inc']['time_on_s']))
        
    if data['hum_dec']['is_on']== True:        
        uasyncio.create_task(hum_dec_s(data['hum_dec']['time_on_s']))
        
    if data['light_ins_inc']['is_on']== True:        
        uasyncio.create_task(light_ins_inc_s(data['light_ins_inc']['time_on_s']))
    
    print("* switches activated")
    return 0

#start event loop and rune entry point coroutine

async def main_prg(parsed,refresh_time=300):#refresh time secs 3600 per hour

    while True:
        print("refreshing main:",time.localtime())
        
        uasyncio.create_task(main_controler(parsed))
        await uasyncio.sleep(refresh_time)
    
    



def main():
    try:
        connect_network()
        try:
            data = get_response()
            #print(data)
            uasyncio.run(main_prg(data))
            
        except:
            print("can get response from server.. check server response")
            return 500
    except:
        print("cant connect with network.. check network configurations")
        return 0





if __name__ == "__main__":
    main()
