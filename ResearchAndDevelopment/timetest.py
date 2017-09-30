import time

(a, b) = (time.time(), time.clock())

time.sleep(15)

(c, d) = (time.time(), time.clock())

timeresult = c - a
clockresult = d - b

clockresult = '{0:.20f}'.format(clockresult)
timeresult = '{0:.20f}'.format(timeresult)

print('timeresult:')
print(timeresult)
print('clockresult:')
print(clockresult)
