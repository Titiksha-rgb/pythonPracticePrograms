line=input('Enter a line:')
lowercount=uppercount=0
digitcount=alphacount=0
for i in line:
  if i.islower():
    lowercount+=1
  elif i.isupper():
    uppercount+=1
  elif i.isdigit():
    digitcount+=1
  if i.isalpha():
    alphacount+=1
print('Number of uppercase letters is:',uppercount)
print('Number of lowercase letters is:',lowercount)
print('Number of alphabets is:',alphacount)
print('Number of digits is:',digitcount)