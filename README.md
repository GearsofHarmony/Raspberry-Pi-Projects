# Raspberry-Pi-Projects
Various projects done on the Raspberry Pi 5

# BME280 Environment Sensor
This project, written in Python, contains two separate scripts. The bme280-test.py script reads from the sensor every minute for 60 minutes and outputs the data into a file. The read_bme280_data.py script reads from the output file and then saves a generated line graph model into a PNG file. The run.sh script will run both Python scripts and setup the Python virtual environment automatically if the directory doesn't exist.
