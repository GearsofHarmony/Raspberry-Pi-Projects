import csv
import bme280
import smbus2
from time import sleep

def scan_i2c_bus(bus_num=1):
	bus = smbus2.SMBus(1)
	devices = []
	for address in range(0x03, 0x77):
		try:
			bus.write_byte(address, 0)
			devices.append(address)
		except:
			pass
	bus.close()
	return devices

def detect_bme280_address():
	devices = scan_i2c_bus()
	bme280_addresses = [0x76, 0x77]
	for address in devices:
		if address in bme280_addresses:
			return address
	return None

wait = 60		#Seconds
time = 60		#Minutes
w_file = "output"

bus=smbus2.SMBus(1)
address=detect_bme280_address()
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
	
bus.close()