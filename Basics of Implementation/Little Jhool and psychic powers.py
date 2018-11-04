n = input()
flag = 0
if len(n) <6:
    print("Good luck!")
    flag = 1
else:
    for i in range(len(n)-5):
        if(n[i] == '0' and n[i+1] == '0' and n[i+2] == '0' and n[i+3] == '0' and n[i+4] == '0' and n[i+5] == '0'):
            print("Sorry, sorry!")
            flag = 1
            break
        elif(n[i] == '1' and n[i+1] == '1' and n[i+2] == '1' and n[i+3] == '1' and n[i+4] == '1' and n[i+5] == '1'):
            print("Sorry, sorry!")
            flag = 1
            break
if flag == 0:
    print("Good luck!")
