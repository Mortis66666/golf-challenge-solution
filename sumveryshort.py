p=[0,0];x=1
while 1:
 p[x:=x^1]|=1<<int(input())
 # print(*["-XO"[(2**i&sum(p))*(-(p[1]>>i&1)-1)]for i in range(9)])
 print(*[(2**i&sum(p))*(-(p[1]>>i&1)-1)for i in range(9)])
 if any(y==y&p[x]for y in[448,56,7,292,146,73,84,273]):print("XO"[x]+" win");break
 if sum(p)==511:print("Tie");break