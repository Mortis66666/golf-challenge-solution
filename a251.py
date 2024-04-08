p=[0,0];x=0
while 1:
 p[x]|=1<<int(input());print(*["-"if(p[0]&(1<<i))+(b:=p[1]&(1<<i))==0else"XO"[b>>i]for i in range(9)])
 if any(y==y&p[x]for y in[448,56,7,292,146,73,84,273]):print("XO"[x]+" win");break
 if p[0]+p[1]==511:print("Tie");break
 x=1-x