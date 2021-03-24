#4.Count the occurence of each word in a line of text.
a=str(input("Enter the words:"))
cd=dict()
words=a.split()
print(words)
for x in words:
  if x in cd:
    cd[x]=cd[x]+1
  else:
    cd[x]=1
print(cd)
