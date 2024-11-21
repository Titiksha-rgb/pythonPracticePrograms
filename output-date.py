num=int(input("Enter the date in MMDDYYYY format:"))
month=num//1000000
rem=num%1000000
date=rem//10000
year=rem%10000
if month==1:
  month='January'
elif month==2:
  month='February'
elif month==3:
  month='March'
elif month==4:
  month='April'
elif month==5:
  month='May'
elif month==6:
  month='June'
elif month==7:
  month='July'
elif month==8:
  month='August'
elif month==9:
  month='September'
elif month==10:
  month='October'
elif month==11:
  month='November'
elif month==12:
  month='December'
else:
  print("There is no such month")

print(month, date,",",year)