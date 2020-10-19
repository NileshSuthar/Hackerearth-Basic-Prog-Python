n = int(input())
arr = input().split(" ")
count = 0
min = int(arr[0])
for i in range(n):
    if(int(arr[i])< min):
        min = int(arr[i])
max = int(arr[0])
for i in range(n):
    if(int(arr[i])> max):
        max = int(arr[i])
for i in range(min,max+1):
    if str(i) not in arr:
        count = 1
if count == 1:
    print("NO")
else:
    print("YES")
