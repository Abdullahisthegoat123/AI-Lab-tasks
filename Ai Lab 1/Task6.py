row = 4
space = 3
count = 1
num = 1

for i in range(row):
    for j in range(space):
        print('', end=' ')

    for k in range(count):
        print(num, end=' ')
        num += 1

    print()        
    space -= 1       
    count += 1 