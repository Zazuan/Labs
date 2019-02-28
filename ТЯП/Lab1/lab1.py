print("a")
a=int(input())
print("b")
b=int(input())
print("c")
c=int(input())
print("k")
k=int(input())
if a == 0 or b == 0:
    print("a<>0 b<>0!!!")
    exit(1)
if a+b+c*((k-a)/b**3) == 0:
    print("a+b+c*((k-a)/b**3)<>0")
    exit(3)
print(" = %f" % ((abs(((a*a/b*b)+c*c*a*a)/(a+b+c*((k-a)/b**3))+c+(k/b-k/a)*c))))

