'''
Guy Shiff - 308577469
Nadav Lotan - 312346406
Sensing - Blynk app & IFTTT
'''

import BlynkLib
import time
import Adafruit_DHT
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import requests
import threading

temperatureSensor = Adafruit_DHT.DHT22
BLYNK_AUTH = 'e6eba6bed75e4b179b85830d8a6f2943'

temperatureSensorPin = 5
CLK = 18
MISO = 23
MOSI = 24
CS = 25

mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

def temperature():
    while True:
        humidityCurVal, temperatureCurVal = Adafruit_DHT.read_retry(temperatureSensor, temperatureSensorPin)
        blynk.virtual_write(0, temperatureCurVal)
        time.sleep(0.5)


def humidity():
    while True:
        humidityCurVal, temperatureCurVal = Adafruit_DHT.read_retry(temperatureSensor, temperatureSensorPin)
        if int(humidityCurVal) > 82:
            requests.post('https://maker.ifttt.com/trigger/humidOver_82/with/key/lfnRM_16wslaPk3UDONUe')
        blynk.virtual_write(1, humidityCurVal)
        time.sleep(0.5)

def potentiometer():
    while True:
        potenValue = mcp.read_adc(0)
        if int(potenValue) == 1023:
            requests.post('https://maker.ifttt.com/trigger/potnInMaxVal/with/key/lfnRM_16wslaPk3UDONUe')
        blynk.virtual_write(2, potenValue)
        time.sleep(0.5)


tempThread = threading.Thread(name='temperature', target=temperature)
humThread = threading.Thread(name='humidity', target=humidity)
potnThread = threading.Thread(name='potentiometer', target=potentiometer)

tempThread.start()
humThread.start()
potnThread.start()

blynk.run()
