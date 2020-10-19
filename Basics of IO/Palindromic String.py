str1 = input()
count = 0
for i in range(int(len(str1)/2)):
    if(str1[i] == str1[len(str1)-1-i]):
        count +=1
if(count == int(len(str1)/2)):
    print("YES")
else:
    print("NO")
