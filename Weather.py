#!/usr/bin/python
import time, datetime, sys, os
import Adafruit_DHT
import Adafruit_BMP.BMP085 as BMP085
from w1thermsensor import W1ThermSensor
 
#Configure DHT sensor
pin = 23    # the GPIO that the DHT11 is connected to.
sensor = Adafruit_DHT.DHT11
 
#Configure BMP180
pressure_sensor = BMP085.BMP085()
 
#Configure DS18B20
accurate_sensor = W1ThermSensor()
 
print 'Starting Up Temperature Monitor'
 
_debug = 1
 
# Continuously get values
while True:
    try:
        # Read values from the DHT sensor if we can
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
 
        # Read value from DS18B20 for more accurate temperature
        temperature_in_celsius = accurate_sensor.get_temperature()
 
        # Read data from BMP180
        pressure = pressure_sensor.read_sealevel_pressure()
        pressure = pressure / 100.0 # 1 mbar = 100 Pa.
 
        if _debug:
            print('BMP180 Data Readout:')
            print('Temp = {0:0.2f} *C'.format(pressure_sensor.read_temperature()))
            print('Pressure = {0:0.2f} Pa'.format(pressure_sensor.read_pressure()))
            print('Altitude = {0:0.2f} m'.format(pressure_sensor.read_altitude()))
            print('Sealevel Pressure = {0:0.2f} mb'.format(pressure))
 
        if humidity is not None and temperature is not None:
            if _debug:
                print('DHT Temp={0:0.1f}*C, DS18B20 Temp={1:0.1f}*C Humidity={2:0.1f}%'.format(temperature, temperature_in_celsius, humidity))
            time.sleep(5)
        else:
            if _debug:
                print('Failed to get reading. Waiting 2 seconds.')
            time.sleep(2)
            continue
 
    except KeyboardInterrupt:
        break
