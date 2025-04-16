import csv
from datetime import datetime
from dateutil import tz
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def get_left_margin(left):
	return datetime(year=left.year, month=left.month, day=left.day, hour=left.hour, minute=left.minute-(left.minute%15), tzinfo= left.tzinfo)

def get_right_margin(right):
	if (right.minute+15) >= 60:
		return datetime(year=right.year, month=right.month, day=right.day, hour=right.hour+1, minute=(right.minute-(right.minute%15)+15)%60, tzinfo= right.tzinfo)
	return datetime(year=right.year, month=right.month, day=right.day, hour=right.hour, minute=(right.minute-(right.minute%15)+15)%60, tzinfo= right.tzinfo)

r_file = "output"
data_x = []
data_y = []

with open(f"{r_file}_{1}", 'r') as csv_r:
	read = csv.reader(csv_r)
	for data in read:
		ts = datetime.strptime(data[0], '%Y-%m-%d %H:%M:%S.%f%z')#.astimezone(tz.tzlocal())#.strftime('%Y-%m-%d %I:%M:%S')
		data_x.append(ts)
		data_y.append((float(data[1]) * 9 / 5) + 32)

fig, ax = plt.subplots()
ax.plot(data_x, data_y, '-g')
ax.xaxis.set_major_locator(mdates.HourLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %I:%M:%S %p', tz.tzlocal()))
ax.xaxis.set_minor_locator(mdates.MinuteLocator(interval=15))

ax.set_xlim([get_left_margin(data_x[0]), get_right_margin(data_x[len(data_x)-1])])
plt.xticks(rotation=30, ha='right')
plt.ylabel("Temperature (F)")
plt.title('Temperature Data Report', fontsize = 20) 
plt.grid()
#plt.legend()
plt.savefig("out_fig", bbox_inches='tight', pad_inches=0.2)
#plt.show()
#"""
