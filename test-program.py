#test program 1
count=0
while count<10:
  print('Hello')
  count+=1
#test program 2
x=10
y=0
while x>y:
  print(x,y)
  x=x-1
  y=y+1
#test program 3
# keepgoing=True
# x=100
# while keepgoing:
#   print(x)
#   x=x-10
#   if x<50:
#     keepgoing=False
#Output:
100
90
80
70
60
50
#Test program 4
# x=45
# while x<50:
#   print(x)
#Test program 5
# for x in [1,2,3,4,5]:
#   print(x)
#Test program 6
# for p in range(1,10):
#   print(p)
#Test program 7
# for z in range(-500,500,100):
#   print(z)
#Test program 8
# x=10
# y=5
# for i in range(x-y*2):
#   print("%",i)
#loop will execute 0 times , since y*2 will be 10 and 10-10 will be 0
#Test program 9
# c=0
# for x in range(10):
#   for y in range(5):
#     c+=1
# print(c)
#The code effectively counts how many times the nested loops execute, which is 50
#Test program 10
# x=[1,2,3]
# counter=0
# while counter<len(x):
#   print(x[counter]*'% ')
#   for y in x:
#     print(y*'* ')
#   counter+=1
# #Test program 11
# for x in 'lamp':
#   print(str.upper(x))
#Output:
# L
# A
# M
# P
#Test program 12
# x='one'
# y='two'
# counter=0
# while counter<len(x):
#   print(x[counter],y[counter])
#   counter+=1
# #Test program 13
# x="apple, pear, peach"
# y=x.split(", ")
# for z in y:
#   print(z)
# The split() method is used to divide the string x into a list of substrings.
# The argument ", " specifies the delimiter to split the string. The delimiter is what separates the elements in the original string.
# The split(", ") operation splits the string at each occurrence of ", ".
#Test program 14
# x='apple, pear, peach, grapefruit'
# y=x.split(', ')
# for z in y:
#   if z<'m':
#     print(str.lower(z))
#   else:
#     print(str.upper(z))
# The split() method splits the string x at each occurrence of ", ".
# It creates a list of substrings.
# This if statement checks whether the fruit name (string z) is lexicographically (alphabetically) less than the string 'm'.
#Test program 15
# for Name in ['Jayes','Ramya','Taruna','Suraj']:
#   print(Name)
#   if Name[0]=='T':
#     break
#   else:
#     print('Finished!')
# print('Got it!')
# #Test program 16
# for i in range(-1,7,-2):
#   for j in range(3):
#     print(i,j)
# However, a step of -2 doesn't make sense with a starting point of -1 and a positive stop value like 7. This is because stepping negatively never reaches or exceeds a positive stop value. Hence, the outer loop does not execute even once.
#Test program 17
# for i in range(1,3,1):
#   for j in range(i+1):
#     print('*')
#Test program 18
# m=3
# n=5
# while n<10:
#   m=n-1
#   n=2*n-m
#   print(n,m)
#Test program 19
#Positive, Negative or Zero
# num=int(input('Enter the number:'))
# if(num<0):
#   print('The number',num,'is negative')
# elif(num==0):
#   print('The number',num,'is equal to 0')
# else:
#   print('The number',num,'is positive')
#Test program 20
# num=int(input('Enter the number:'))
# if num%2==0:
#   print(True)
# else:
#   print(False)
#Test program 21
## num=float(input("Enter the number of years:"))
# seconds=num*365*24*60*60
# print("There are",seconds,'seconds in',num,'years')
#Test program 22
# num1=int(input("Enter the first number:"))
# num2=int(input('Enter the second number:'))
# if num1%num2==0:
#   print(num1,"is completely divisible by",num2)
# else:
#   print(num1,'is not completely divisible by',num2)
#Test program 23
day=input('Enter the day on 1st January:')
num=int(input('Enter number between 2 and 365 inclusively:'))
if day=='sunday':
  if num%7==1:
    print('Sunday')
  elif num%7==2:
    print('Monday')
  elif num%7==3:
    print('Tuesday')
  elif num%7==4:
    print('Wednesday')
  elif num%7==5:
    print('Thursday')
  elif num%7==6:
    print('Friday')
  elif num%7==0:
    print('Saturday')
elif day=='monday':
  if num%7==1:
    print('Monday')
  elif num%7==2:
    print('Tuesday')
  elif num%7==3:
    print('Wednesday')
  elif num%7==4:
    print('Thursday')
  elif num%7==5:
    print('Friday')
  elif num%7==6:
    print('Saturday')
  elif num%7==0:
    print('Sunday')
elif day=='tuesday':
  if num%7==1:
    print('Tuesday')
  elif num%7==2:
    print('Wednesday')
  elif num%7==3:
    print('Thursday')
  elif num%7==4:
    print('Friday')
  elif num%7==5:
    print('Saturday')
  elif num%7==6:
    print('Sunday')
  elif num%7==0:
    print('Monday')
elif day=='wednesday':
  if num%7==1:
    print('Wednesday')
  elif num%7==2:
    print('Thursday')
  elif num%7==3:
    print('Friday')
  elif num%7==4:
    print('Saturday')
  elif num%7==5:
    print('Sunday')
  elif num%7==6:
    print('Monday')
  elif num%7==0:
    print('Tuesday')
elif day=='thursday':
  if num%7==1:
    print('Thursday')
  elif num%7==2:
    print('Friday')
  elif num%7==3:
    print('Saturday')
  elif num%7==4:
    print('Sunday')
  elif num%7==5:
    print('Monday')
  elif num%7==6:
    print('Tuesday')
  elif num%7==0:
    print('Wednesday')
elif day=='friday':
  if num%7==1:
    print('Friday')
  elif num%7==2:
    print('Saturday')
  elif num%7==3:
    print('Sunday')
  elif num%7==4:
    print('Monday')
  elif num%7==5:
    print('Tuesday')
  elif num%7==6:
    print('Wednesday')
  elif num%7==0:
    print('Thursday')
elif day=='saturday':
  if num%7==1:
    print('Saturday')
  elif num%7==2:
    print('Sunday')
  elif num%7==3:
    print('Monday')
  elif num%7==4:
    print('Tuesday')
  elif num%7==5:
    print('Wednesday')
  elif num%7==6:
    print('Thursday')
  elif num%7==0:
    print('Friday')
else:
  print("Invalid day, enter in all small")
#Test program 24
