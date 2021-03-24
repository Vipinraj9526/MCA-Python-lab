#2.Display future leap year from current year to a final year entered by user.

y1=int(input("Enter the current year:"))
y2=int(input("Enter the last year:"))
for x in range(y1,y2+1):
   if x%4==0 and x%100!=0 or x%400==0:
      print(x)
