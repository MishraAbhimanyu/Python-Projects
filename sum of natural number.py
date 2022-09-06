n=int(input("Enter the number upto which you want to add\n"))
sum=0
for i in range(1,n+1):
    sum=i+sum
print("Addition of natural numbers up to",n,"is",sum)
