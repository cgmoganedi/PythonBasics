from decimal import *
print (getcontext())
getcontext().prec = 10

a = Decimal(10.375)

print (a)
print (2 * a)
