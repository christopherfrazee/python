# Python 2.7
##########################################
# This code has no fuctional purpose     #
# other than to serve as coding practice #
##########################################
import math
import csv
import re

Count = 1
MaxCount = 8
Increment = 1
LowNumber = 3
HighNumber = 9
PowNumber = 7
Power = 2
Ips = ["43.34.133.6", "43.78.99.7", "10.1.1.1"]
NewIp = "192.168.0.1"

MathPowOut = math.pow(PowNumber, Power)
print "{} to the {} power is {}".format(PowNumber, Power, MathPowOut)

print "Count with while loop and increment by {}\n".format(Count)
while Count < 11:
    print Count
    Count = Count + Increment
else:
    print 'Counting complete.'

for RangeNum in range(LowNumber, HighNumber):
    print(RangeNum)
else:
    print "Counting by range {} - {} complete".format(LowNumber, HighNumber)

print "working with printing arrays\n"
print "{}\n{}\n{}\n".format(Ips[0], Ips[1], Ips[2])

print "append elements to array\n"
Ips.append(NewIp)
for Ip in Ips:
    print(Ip)
print "sorted arrays\n"
Ips.sort(key=lambda ip: map(int, ip.split('.')))
for Ip in Ips:
    print(Ip)

print "read from csv\n"
with open('test.csv') as csvfile:
    Row = csv.reader(csvfile, delimiter=',')
    for Column in Row:
        print(Column[0],Column[1],Column[2])
        Ips.append(Column[0])
        Ips.append(Column[1])
	Ips.append(Column[2])
print "append new IP's from csv, sort then print them/n"
Ips.sort(key=lambda ip: map(int, ip.split('.')))
for Ip in Ips:
    regex = re.compile("^192.168.|^10.1.")
    if re.match(regex, Ip):
	print "{} is non puplic routable. SKIPPING /n".format(Ip)
    else:
        print "{} OK".format(Ip)
