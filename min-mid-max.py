num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
if num1>num2:
  if num2>num3:
    a,b,c=num3,num2,num1
  else:
    a,b,c=num2,num3,num1
elif num2>num3:
   if num3>num1:
    a,b,c=num1,num3,num2
   else:
    a,b,c=num3,num1,num2
elif num3>num1:
   if num1>num2:
     a,b,c=num2,num1,num3
   else:
     a,b,c=num1,num2,num3
print("min:",a,"mid:",b,"max:",c)
#in questions like these, include all cases or you might face errors