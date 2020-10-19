ans = 1
n = int(input())
num = input()
p = num.split(" ")
for i in range(n):
    ans = ans*int(p[i])%1000000007
print(ans)
