import mraa 
import time
print (mraa.getVersion()) 
led = mraa.Gpio(23) 
led.dir(mraa.DIR_OUT) # set led direction as output
led.write(0) 
 
while True: 
    led.write(1) #turn on LED 
    time.sleep(0.5) # 500msec delay

    led.write(0) #turn off LED
    time.sleep(0.5) #500msec delay
