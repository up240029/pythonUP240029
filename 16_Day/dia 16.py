#1
import datetime
hoy =datetime.datetime.now()
print(hoy)
#2
formateoHoy = hoy.strftime("%m/%d/%Y, %H:%M:%S")
#3
from datetime import datetime
dateString = "5 December, 2019"
print("dateString =", dateString)
dateObject = datetime.strptime(dateString, "%d %B, %Y")
print("dateObject =", dateObject)
#4
from datetime import datetime, timedelta, date
today = date(year=2025, month=4, day=2)
newYear = date(year=2026, month=1, day=1)
time= newYear - today
print("Este tiempo falta para año nuevo: ", time) 
#5
hoy = date(year=2025, month=4, day=2)
antes = date(year=1972, month=1, day=1)
times= hoy- antes
print(times)
#6
# se pude utilizar para modificar al momento el tiempo o para orientarte sobre que hora o fecha hay en otro lado del mundo
# en este mismo momento