s=int(input("Enter start\n"))
e=int(input("Enter end\n"))
j=int(input("Enter jump\n"))
pro=1
for i in range (s,e+1,j):
    pro=pro*i
    print(i)
print("product of this series =",pro)
