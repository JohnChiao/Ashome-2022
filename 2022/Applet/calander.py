MODULE = "[calendar]"
import datetime
import calendar
def gettime():
    print(MODULE+'现在是：', datetime.datetime.now(), end=',  ')
    weekday = datetime.datetime.now().weekday()
    weekdlist = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    print(MODULE+weekdlist[weekday])

def run(year):
    cal = calendar.calendar(year)
    print(cal)

