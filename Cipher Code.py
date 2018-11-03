'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
import math
inp = input()
inp1 = []
k = int(input())
for i in range(len(inp)):
    if(ord(inp[i])>=97 and ord(inp[i])<=122):
        if(ord(inp[i])+k > 122):
            inp1.append(chr(ord(inp[i])+k-(math.ceil((ord(inp[i])+k-122)/26.0)*26)))
        else:
            inp1.append(chr(ord(inp[i])+k))
    if(ord(inp[i])>=65 and ord(inp[i])<=90):
        if(ord(inp[i])+k > 90):
            inp1.append(chr(ord(inp[i])+k-(math.ceil((ord(inp[i])+k-90)/26.0)*26)))
        else:
            inp1.append(chr(ord(inp[i])+k))
    if(ord(inp[i])>=48 and ord(inp[i])<=57):
        if(ord(inp[i])+k > 57):
            inp1.append(chr(ord(inp[i])+k-(math.ceil((ord(inp[i])+k-57)/10.0)*10)))
        else:
            inp1.append(chr(ord(inp[i])+k))
    if(ord(inp[i])>=33 and ord(inp[i])<=47):
        inp1.append(inp[i])
    if(ord(inp[i])>=58 and ord(inp[i])<=64):
        inp1.append(inp[i])
    if(ord(inp[i])>=91 and ord(inp[i])<=96):
        inp1.append(inp[i])
    if(ord(inp[i])>=123 and ord(inp[i])<=126):
        inp1.append(inp[i])
    

str1 = ''.join(inp1)
print(str1)
