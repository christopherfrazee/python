##########################################
# This code has no real fuctional purpose#
# other than to serve as coding practice #
##########################################

################################
# Python library configuration #
################################

import math
import csv
import re
import sys
import requests
import ipaddress

#########################
# initial configurables #
#########################

Count = 1
MaxCount = 8
Increment = 1
LowNumber = 3
HighNumber = 9
PowNumber = 7
Power = 2
Ips = ["43.34.133.6", "43.78.99.7", "10.1.1.1"]
NewIp = "192.168.0.1"
OutFile = "test_output.txt"
IndexFile = "index.html"
WebSite = 'www.google.com'
Header1 = 'GET / HTTP/1.1\r\nHost: '
Header2 = '\r\nConnection: close\r\n\r\n'
HttpHeader = Header1 + WebSite + Header2
InputCsvFile = 'test.csv'
Key = '\'{:>3}{:>3}{:>3}{:>3}\'.format(*key.split(\'.\'))'

########################
# do a little math fun #
########################

MathPowOut = math.pow(PowNumber, Power)
print('{} to the {} power is {}'.format(PowNumber, Power, MathPowOut))

################
# incrementing #
################

print('Count with while loop and increment by {}'.format(Count))
while Count < 11:
    print(Count)
    Count = Count + Increment
else:
    print('Counting complete.')

##################
# numeric ranges #
##################

for RangeNum in range(LowNumber, HighNumber):
    print(RangeNum)
else:
    print('Counting by range {} - {} complete'.format(LowNumber, HighNumber))

##########################
# put data in array/list #
##########################

print('working with printing arrays')
print('{}\n{}\n{}\n'.format(Ips[0], Ips[1], Ips[2]))

####################################
# append elements to an array/list #
#################################### 

print('append elements to array')
Ips.append(NewIp)
for Ip in Ips:
    print(Ip)
print('sorted IP addresses in a list')

###############################
# sort a list of IP addresses #
###############################

#Ips.sorted(ip,key=lambda)
for Ip in sorted(Ips):
    print(Ip)

#############################
# do a little file handling #
#############################

print('practice reading from csv file')
with open(InputCsvFile) as csvfile:
    Row = csv.reader(csvfile, delimiter=',')
    for Column in Row:
        print(Column[0],Column[1],Column[2])
        Ips.append(Column[0])
        Ips.append(Column[1])
        Ips.append(Column[2])
print('append new IP\'s from csv, sort then print them')
f = open(OutFile,'w')
print('print externally routable IP addresses to a file')

#####################################
# iterate through list, filter data #
#####################################

for Ip in Ips:
    regex = re.compile("^192.168.|^10.1.")
    if re.match(regex, Ip):
        print('{} is non puplic routable. SKIPPING'.format(Ip))
    else:
        print('{} OK'.format(Ip))
        f.write(' '.join(('IP:', str(Ip), "\n")))

###########################################
# pull down some data from a https server #
###########################################
f = open(IndexFile,'w')
indexFile = requests.get("https://www.google.com")
indexFile.status_code
200
f.write(indexFile.text)    # dump the results to a file
  
