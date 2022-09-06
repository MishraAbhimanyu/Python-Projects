a=int(input("Enter the first number \n"))
ch=input("Enter choice of operation \n")
b=int(input("Enter the second choice \n"))
if ch=='+':
        print("Your answer is",a+b)
elif ch=='-':
        print("Your answer is",a-b)    
elif ch=='*':
        print("Your answer is",a*b)
elif ch=='/':
        print("Your answer is ",a/b)
elif ch=='%':
        print ("Your answer is",a%b)
else:
    print("Invalid Choice")
