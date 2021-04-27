
def calculate_factorial_recursive(number):
    if number==1:
        return number
    else :
        return number*calculate_factorial_recursive(number-1)
    
def calculate_factorial(number):
    factorial=1
    for i in range(1,number+1):
        factorial*=i
    return factorial


x = int(input("Enter number: "))
print("Factorial of:",x,"=>",x,"!=",calculate_factorial_recursive(x))
print("Factorial of:",x,"=>",x,"!=",calculate_factorial(x))