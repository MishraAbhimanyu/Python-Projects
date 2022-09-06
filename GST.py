value=int(input("Enter Value According to Menu \n Press 1 for GST & Bill calculation \n Press 2 for UnGSTing the bill\n"))

if value==1:
    a=float(input("Enter the total amount on which gst and bill is to be calculated \n"))
    gst=float(a*0.18)
    bill=a+gst
    print("Amount of GST is\n",gst)
    print("Total bill to be paid is \n",bill)
elif value==2:
    a=float(input("Enter the total amountwith GST on which value to be calculated \n"))
    bill2=(a/118)*100
    g=a-bill2
    print("Amount of GST is",g)
    print("Bill without GST",bill2)
else:
    print("Please enter a valid Value")
    
