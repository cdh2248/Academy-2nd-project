from datetime import datetime, timedelta


i = "20130729"

a = datetime.strptime(i, "%Y%m%d")

print(a)