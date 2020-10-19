n = int(input())
sm = []
for i in range(n):
    p = input()
    sum = int(p[0])
    for i in range(0,len(p)-2,2):
        if p[i+1] == "+":
            sum = sum+int(p[i+2])
        elif p[i+1] == "-":
            sum = sum-int(p[i+2])
    sm.append(sum)
print(max(sm))
        
