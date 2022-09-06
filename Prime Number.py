num=int(input("Enter a number\n"))
if num==1 or num==0:
    print("Number is Neither Prime Nor Composite")
else:
    for i in range(2,num):
            if num%i==0:
                print("Number is not prime")
                
                break   
    else:
        print("Number is prime")
            
