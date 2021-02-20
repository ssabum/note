a = [1, 2, 3, 4]

for i in range(1<<len(a)):
    for j in range(len(a)):
        if i & (1<<j):
            print(a[j], end="")
        else:
            print('0', end="")
    print('')