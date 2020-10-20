x,k = input().split(" ")
k = int(k)
for i in range(len(x)):
    if(x[i] != 57):
        if(k>0):
            print(9,end ="")
            k-=1
        else:
            print(x[i],end ="")
    else:
        print(9,end ="")
        
  #correction required
