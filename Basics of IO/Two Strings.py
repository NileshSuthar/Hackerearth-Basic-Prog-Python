str1 = []
n = int(input())
for i in range(n):
    s1 = input()
    str1 = s1.split(" ")
    if(sorted(str1[0]) == sorted(str1[1])):
        print("YES")
    else:
        print("NO")
