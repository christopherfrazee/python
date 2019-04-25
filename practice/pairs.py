import math
import os
import sys

ar = ["50", "100", "25", "50", "75", "100", "75" , "100"]
result = 0
lastnum = 0
for n in sorted(ar):
    if n == lastnum:
        result = result + 1
        lastnum = 0
    else:
        lastnum = n
print(result)
