N=int(input("Enter the number:"))
if N>0:
  sum=0
  for i in range(N,2*N+1):
    sum+=i
  print("Sum from N to 2N is:",sum)
elif N<0:
  sum=0
  for i in range(N,2*N-1,-1):
    sum+=i
  print("Sum from 2N to N is:",sum)
else:
  print("Number should not be 0, input either a positive or a negative integer.")