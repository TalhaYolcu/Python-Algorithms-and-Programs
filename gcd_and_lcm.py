def gcd(a,b):
    if(a%b==0):
        return b
    else:
        return gcd(b,a%b)
    
def lcm(a,b):
    return (a*b/gcd(a,b))

x=int(input("Enter large number:"))
y=int(input("Enter small number:"))

if x<y:
    temp=x
    x=y
    y=temp
    
print("Greatest common divisior of",x,"and",y,"is:",gcd(x,y))
print("Least common multiple of",x,"and",y,"is",lcm(x,y))