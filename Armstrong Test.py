n=input("Enter a numner\n")
print(n)
l=len(n)
n=int(n)
print(l)
arm=0
temp=n
while n>0:
    rem=n%10
    arm=arm+rem**l
    n=n//10
if arm==temp:
    print(temp, "Number is Armstrong")
else:
    print(temp, "Number is not Armstrong")
