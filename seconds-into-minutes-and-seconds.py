number=int(input("Enter the number of seconds:"))
minutes=number//60
seconds=number%60
if(minutes==0):
  print("No. of seconds is:",seconds)
else:
  print("No. of minutes is:",minutes,"and number of seconds is:",seconds)
