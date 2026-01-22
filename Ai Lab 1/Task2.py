listof = []
for i in range(10):
    listof.append(int(input(("Enter a number: "))))
print(listof)
def prime(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i ==0:
            return False
    return True

for i in range(10):
    if prime(listof[i]):
        print(listof[i],'is prime')
    else:
        print(listof[i],'is not prime')