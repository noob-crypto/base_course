znam = int(input())
pervoe = int(input())
n = int(input())
i = 1

while i < n + 1: 
    j = i - 1
    q = znam ** j
    bn = pervoe * q
    print (bn)
    j += 1