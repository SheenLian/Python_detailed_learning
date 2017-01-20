import time
import calendar
tick = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", tick)
print('Below is a time tuple:')
print(time.localtime())

print('Local readable time(asctime): ', time.asctime())
cal = calendar.month(2017,1)
print('getting calendar of a specific month: \n', cal)

print('~~~~~~~built in for time module~~~~~~~~')
print('time.clock: ', time.clock())
print('time.gmtime: ', time.gmtime())
print('make time: ', time.asctime(time.localtime(time.mktime(time.localtime()))))
print('~~~~~~~~~~time to sleep~~~~~~~~~~~~~')
print ("Start : %s" % time.ctime())
time.sleep( 1 )
print ("End : %s" % time.ctime())

print('strftime (strptime is the reverse): ', time.strftime('%A %B %d %Y %H:%M:%S', time.localtime()))
#print(calendar.calendar(theyear= 2017, w=2, l=1, c=6))
print(calendar.firstweekday())# don't know
print('calendar.isleap: ', calendar.isleap(2016))
print('calendar.leapdays: ', calendar.leapdays(2016, 2017))
print(calendar.month(theyear= 2017, themonth=1, w=2, l=1))
print(calendar.monthcalendar(2017, 1))
print(calendar.monthrange(2017, 1))
calendar.prcal(theyear= 2017, w=2, l=1, c=6)


