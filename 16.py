d1,d2=map(int,input().split())
for d3 in range(d1,d2):
   if d3>1:
      for i in range(2,d3):
        if(d3%i)==0:
          break
      else:
          print(d3,end=" ")
