h = int(input()) # input height
w = int(input()) # input width
data = bin(int(input()))[2:] #input base10
# if data does not align with width x height then add extra zeroes in front until it does.
while len(data) < w*h:
    data = '0' + data
# slice data in sublists and seperate numbers
data = [[data[i::w]] for i in range(0, len(data) // h)]

n = 0
data2 = []
for i in data:
    data2 += [list(i) for i in data[n]]
    n += 1

# loop through all data and determine answer
n = 0
f = 0
ans = 0
for x in data:
    for i in data2[n][::-1]:
        if i == '1':
            f += 1
            if f > ans:
                ans = f
        else:
            n += 1
            f = 0
            break
        
# print the answer
print(ans)