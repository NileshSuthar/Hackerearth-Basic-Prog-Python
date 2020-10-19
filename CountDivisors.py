p = input()
p = p.split(" ")
q = int(p[0])
r = int(p[1])
k = int(p[2])
count = 0
for i in range(q, r + 1):
    if i % k == 0:
        count += 1
print(count)
print("done")
