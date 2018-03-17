from datetime import date


y1 = 2014
m1 = 7
d1 = 2
y2 = 2014
m2 = 7
d2 = 11

from datetime import date
f_date = date(y1, m1, d1)
l_date = date(y2, m2, d2)
delta = l_date - f_date
print(delta.days)
