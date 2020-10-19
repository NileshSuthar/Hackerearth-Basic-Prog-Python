n = int(input())
for i in range(n):
    s = int(input())
    if(s%12 == 0):
        st = s-11
        print(st, "WS")
    else:
        k = int(s/12)
        sn = 12*k +6
        st = 2*sn-s+1
        nm = st-k*12
        if(nm == 1 or nm == 12):
            print(st, "WS")
        elif(nm == 2 or nm == 11):
            print(st, "MS")
        elif(nm == 3 or nm == 10):
            print(st, "AS")
        elif(nm == 4 or nm == 9):
            print(st, "AS")
        elif(nm == 5 or nm == 8):
            print(st, "MS")
        elif(nm == 6 or nm == 7):
            print(st, "WS")

