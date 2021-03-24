#6 Store a list of first names. Count the occurrences of ‘a’ within the list
 
li=[]
c=0
n=int(input("Enter no.of names:"))
for x in range (n):
   name=input("enter first names:")
   li.append(name)
for x in li:
   for y in x:
     if 'a' in y:
       c=c+1
print("number of 'a' is:",c)
