n=int(input("Enter the number upto which you want to add\n"))
sum=0
for i in range(1,n+1):
    p=i*i
    sum=p+sum
    print("Series of square is",p)
print("Addition of squares of natural numbers up to",n,"is",sum)
