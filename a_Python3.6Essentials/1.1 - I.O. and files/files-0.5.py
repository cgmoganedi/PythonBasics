fd1 = open('file')
#first100bytes = fd1.read(100)
#line1 = fd1.readline()
for line in fd1:
    doMyProcess(line)
