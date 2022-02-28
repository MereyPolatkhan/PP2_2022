from datetime import datetime, timedelta, time

date1 = datetime.strptime("20 September 2004, 07:00:00", "%d %B %Y, %H:%M:%S") # my bd
date2 = datetime.now() 


def diff(d2, d1):
    # should be d2 > d1
    t = d2 - d1 # X_days, hh:mm:ss

    return (t.days * 24 * 60 * 60 + t.seconds)

print(f'seconds: {diff(date2, date1)}')