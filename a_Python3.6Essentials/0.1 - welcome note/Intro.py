principal = 1000    # initial amout
rate = 0.05         # compunding interest rate of 5.00%
numyears = 5        # number of years
year = 1            # where you at

while year <= numyears :
    principal = principal * (1 + rate)
    print ( "Year = %3d " % (year), " : Principal = %0.2f " % (principal) ) # Remainder : Python3.*
    year += 1


print ("Hello World")
print ("{0:3d} {1:0.2f}".format(year, principal))
