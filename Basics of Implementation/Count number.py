*RTE in one case*

t = int(input())
count=0
for i in range(t):
    n = int(input())
    s = input()
    for j in range(n):
        if(s[j] >=str(0) and s[j]<=str(9)):
            if(s[j+1] >=str(0) and s[j+1]<=str(9)):
                continue
            else:
                count+=1
    print(count)
