n = int(input("Enter the limit:"))
f,s = 0,1
for i in range(n):
  t = f+s
  print(f,end = ' ')
  f,s = s,t
  
