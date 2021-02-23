a = [0,0,0,0]
b = [0,0,1,1]

for i in range(4):
    if a[i] != b[i]:
        a[i:] = b[i]

print(a)