import time
import datetime

ticks = time.time()
print(ticks)

timeData = time.localtime()
print(timeData)
print(timeData.tm_year)

timeData = time.localtime(10)
print(timeData)
print(timeData.tm_year)

result = time.asctime( time.localtime() )
print(result)

timeData = time.localtime()
print(time.strftime("%d/%m/%Y %H:%M:%S ", timeData))


timeStr = "17:23:45 08.12.2021"
timeData = time.strptime(timeStr, "%H:%M:%S %d.%m.%Y")
print(timeData)

i = 0
while i < 12:
    time.sleep(0.0005)
    print(time.asctime(time.localtime()))
    i += 1

tStart = time.perf_counter()
time.sleep(0.0001)
tEnd = time.perf_counter()
print("Code took: ", (tEnd-tStart), "seconds")


datetimeObj = datetime.datetime.now()
print(datetimeObj)
#print(dir (datetimeObj))
datetimeObj = datetime.datetime(2025, 3, 10)
datetimeObj = datetime.datetime(2025, 3, 10, 22, 59, 59)
print("date: ", datetimeObj.date())
print("date: ", datetimeObj.time())
print("timestamp: ", datetimeObj.timestamp())
print("today: ", datetimeObj.today())
print("year: ", datetimeObj.year)
print("month: ", datetimeObj.month)
print("day: ", datetimeObj.day)
print("hour: ", datetimeObj.hour)
print("minute: ", datetimeObj.minute)
print("second: ", datetimeObj.second)


print("format: ", datetimeObj.strftime("%H:%M:%S %d.%m.%Y"))

datetimeObj = datetimeObj.now()
print("format: ", datetimeObj.strftime("%H:%M:%S %d.%m.%Y"))


datetime1 = datetime.datetime(2025,1,1,23,59,59)
datetime2 = datetime.datetime(2030,1,1,23,59,59)

print( datetime2 > datetime1 )
print( datetime2 < datetime1 )

date1 = datetime.date(2025,1,1)
date2 = datetime.date(2027,1,1)

print( date1 < date2 )
print( date1 > date2 )
