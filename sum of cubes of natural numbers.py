n=int(input("Enter the number upto which you want  cube of natural numbers to be added\n"))
sum=0
for i in range(1,n+1):
    p=i*i*i
    sum=p+sum
    print("cube series is",p)
print("Sum of cubes up to",n,"is",sum)
