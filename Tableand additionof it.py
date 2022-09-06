n=int(input("Enter the number for which you want table\n"))
e=int(input("Enter upto the number you want table\n"))
sum=0;

for i in range(1,e+1):
    t=n*i;
    sum=t+sum;
    
print("sum of ",n,"up to",e,"is",sum)
