s=int(input("Enter start number\n"))
print("Start is \t",s)
e=int(input("Enter End Number\n"))
print("End Number is \t",e)
i=2
while e>=s:
    rem=s%i
    if rem==0:
            print(s,"Number is not prime")
        else:
            print(s,"Number is prime")
        break
    i=i+1
