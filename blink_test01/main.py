import time
from machine import Pin

LED_Pin = Pin(27, Pin.OUT)

while True:
    LED_Pin.on()
    time.sleep_ms(500)
    LED_Pin.off()
    time.sleep_ms(500)