n = int(input())
p = input()
p = p.split(" ")
min = p[0]
max = p[0]
for i in range(n):
    if p[i] < min:
        min = p[i]
for i in range(n):
    if p[i] > max:
        max = p[i]
print(min+max)
