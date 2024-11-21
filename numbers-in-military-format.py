num1=int(input("Please enter the first time:"))
num2=int(input("Please enter the second time:"))
if num1>=num2:
  diff=num1-num2
  hours=diff//100
  minutes=diff%100
elif num2>num1:
  diff=num2-num1
  hours=diff//100
  minutes=diff%100
print(hours,"hours",minutes,"minutes")