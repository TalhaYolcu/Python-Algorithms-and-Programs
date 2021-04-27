def fibonacci(a):
    if a<=2:
        return 1
    else:
        return fibonacci(a-1)+fibonacci(a-2)

x=int(input("Enter index:"))
print("Sequence:")
for i in range(x+1):
    print(fibonacci(i),end=" ")