p=[0,0];x=1
while 1:
 p[x:=x^1]|=1<<int(input());print(*[["XO","-"][(p[0]&2**i)+(b:=p[1]&2**i)==0][-b>>i]for i in range(9)])
 if any(y==y&p[x]for y in[448,56,7,292,146,73,84,273]):print("XO"[x]+" win");break
 if sum(p)==511:print("Tie");break