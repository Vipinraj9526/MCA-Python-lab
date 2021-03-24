#5.Prompt the user for a list integers.For all value grater than 100,store'over' instead.

list=[]
a=int(input("Enter the no of values to be inserted:"))
for x in range(a):
   n=int(input("Enter the value"))
   if n<=100:
      list.append(n)
   else:
       list.append('over')
print(list)
