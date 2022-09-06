a=int(input("Enter the number\n"))
if a==0:
    print(a,"is neither even nor odd number")
else:
    if a%2==0:
        if a>0:
            print(a,"is a positive even number")
        else:
            if a!=0:
                print(a,"is a negetive even number")
    else:
        if a<0:
            print(a,"is a negative odd number")
        else:
            print(a,"is a positive odd number")
