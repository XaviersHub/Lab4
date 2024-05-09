import socket
import time
from time import sleep

from hal import hal_input_switch as in_sw
from hal import hal_led as led

def blink_length_10Hz(seconds):
    led.init()
    length = seconds * 10
    for i in range(length):
        led.set_output(0,1)
        time.sleep(0.1)



def led_blinker():
    i = True
    while i == True:
        in_sw.init()
        led.init()

        i = True
        switch = in_sw.read_slide_switch()
        while switch == 1: #switch is to the left
            led.set_output(0, 1)
            time.sleep(1)

            led.set_output(0, 0)
            time.sleep(1)
            switch = in_sw.read_slide_switch()


                    

        while switch == 0:  #switch is to the right
            blink_length_10Hz(5) 
            led.set_output(0,0)
            time.sleep(2)
            switch = in_sw.read_slide_switch()
        switch = in_sw.read_slide_switch()

def main():
    led_blinker()




if __name__ == "__main__":
    main()