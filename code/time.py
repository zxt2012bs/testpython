import time

currenttime = time.time()

totalSeconds = int(currenttime)

currentSecond = totalSeconds % 60

totalMinutes = totalSeconds //60

currentMinute = totalMinutes % 60

totalHours = totalMinutes // 60

currentHour = totalHours % 24 + 8

print("当前时间是", currentHour, ":", currentMinute, ":", currentSecond, "GMT+8 北京")
