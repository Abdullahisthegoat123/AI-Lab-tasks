def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+ fibonacci(n-2)
num = int(input("Enter a number: "))
print("The fibonacci sequence upto n is: ")

for i in range(num):
    print(fibonacci(i))