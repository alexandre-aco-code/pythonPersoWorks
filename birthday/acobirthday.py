from datetime import date

today = date.today()
bday = date(today.year, 1, 8)
diff = (bday-today).days


if diff > 0:
    print("ACo Birthday is in %d days" % diff)
else:
    print("ACo Birthday is in %d days" % (diff+365))
