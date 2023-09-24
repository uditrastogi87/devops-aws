c=1
for i in range(4):
    for j in range(i+1):
        print(c, end='')
        c += 1
    print()

for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print()
