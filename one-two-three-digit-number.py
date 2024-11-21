num=int(input("Enter the number:"))
if(num>=0 and num<10):
  print(num,"is a single digit number.")
elif(num>=10 and num<100):
  print(num,"is a two digit number.")
elif(num>=100 and num<1000):
  print(num,"is a three digit number.")
else:
  print("Not a part of exercise.")