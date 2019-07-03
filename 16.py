d1,d2=map(int,input().split())
for i in range(d1,d2):
 if i>1:
  for i in range(2,i):
   if(i%2)==0:
    break
   else:
    print(i,end=" ")
