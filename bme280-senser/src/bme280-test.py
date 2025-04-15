import csv
import bme280
import smbus2
from time import sleep

port = 1
address = 0x77
bus = smbus2.SMBus(port)
wait = 60		#Seconds
time = 2		#Minutes
w_file = "output"

cal_param = bme280.load_calibration_params(bus, address)

def read_all():
	bme280_data = bme280.sample(bus, address, cal_param)
	return (bme280_data.timestamp, bme280_data.temperature) #, bme280_data.humidity, bme280_data.pressure

#for xx in range(1, 2):
with open(f"{w_file}_{1}", 'w') as csv_w:
	write = csv.writer(csv_w)

	for x in range(0,time):
		write.writerows([read_all()])
		sleep(wait)
	
