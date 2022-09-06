n=int(input("Enter a number\n"))
i=2
if n==0 or n==1:
    print("Number is neither prime nor composite")
else:
    while i<n:
        rem=n%i
        i=i+1
        if rem==0:
            print("Number is not prime")
            break
    else:
            print("Number is prime")
