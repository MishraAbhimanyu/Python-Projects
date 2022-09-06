n=int(input("Enter the numner\n"))
temp=n
rev=0
rem=0
while n>0:             
    rem=n%10
    rev=rev*10+rem      
    n=n//10
print(rev)
if rev==temp:
    print("Number is pelindrom")
else:
    print("Number is Not Pelindrom")
    
