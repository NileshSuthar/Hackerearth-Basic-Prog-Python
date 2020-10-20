p = input()
p = p.split(" ")
l = int(p[0])
r = int(p[1])
k = int(p[2])
count = 0
for i in range(l,r+1):
    if(i%k == 0):
        count+=1
print(count)
