
def findroot(a,b,c):
    delta=b*b-4*a*c
    if delta<0:
        print("There is no real root of this equation")
        return
    elif delta==0:
        print("There is 2 root and they are same")
    else:
        print("There is 2 different root")
    x1=(-b-delta**0.5)/2*a
    x2=(-b+delta**0.5)/2*a
    return (x1,x2)

a = int(input("Enter coefficent of x^2: "))
b = int(input("Enter coefficent of x: "))
c = int(input("Enter the constant: "))

sonuc=[findroot(a,b,c)]

print(sonuc)


