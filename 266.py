w1=int(input())
w2=list(map(int,input().split()[:w1]))
w2.sort()
for i in w2:
   print(i,end=" ")
