import time         #timeをインポート
from machine import Pin #GPIO用

led = Pin(27, Pin.OUT)  #27ピンをインポート

def run():              #対話型コマンドでblink.run()を実行するとLチカが実行される
    for i in range(10):
        led.value(1)
        time.sleep(1)
        led.value(0)
        time.sleep(1)