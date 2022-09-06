n=(input("Enter Your Name \n"))
print (n)
p= int (input("Enter Amount Given as Principal\n "))
print (p)
r=float (input ("Enter Rate of Interest (Without %)\n"))
print (r)
t=float(input ("Enter Number Of Years\n"))
print (t)
i= ((p*r*t)/100)
a= (p+i)
print ("Recheck the value entered",n," \n Principal",p," \n Rate of Interest",r,"\n Time in Years",t)
op=int(input("If all values entered is correct - Press 1 or Press 0 \n"))
if op==1:
    print ("Simple Interest accumulated is ",i)
    print("Total amount to be paid by ",n ,"is" , a)
else:
    print("Enter the correct values again")

