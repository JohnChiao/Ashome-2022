MODULE = "cld"
import datetime
import calendar
def gettime():
    print("["+MODULE+"]"+'现在是：', datetime.datetime.now(), end=',  ')
    weekday = datetime.datetime.now().weekday()
    weekdlist = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    print("["+MODULE+"]"+weekdlist[weekday])

def cld(year = 0):
    stryear = str(datetime.datetime.now())
    intyear = int(stryear[0:4])
    cal = calendar.calendar(year if year else intyear)
    print(cal)

