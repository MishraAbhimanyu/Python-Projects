n=input("enter a number\n")
l=len(n)
n=int(n)
t=n
a=0
while n>0:
    r=n%10
    a=a+r**l
    n=n//10
if t==a:
    print(t,"Is an Armstrong Number")
else:
    print(t,"Is not an Armstrong Number")
