s=int(input("Enter start\n"))
e=int(input("Enter end\n"))
j=int(input("Enter jump\n"))
sum=0
for i in range (s,e+1,j):
    sum=sum+i
    print(i)
print("addition of this series =",sum)
