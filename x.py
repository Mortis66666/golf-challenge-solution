O=X=Q=0;B,p=['-']*9,print
while'-'in B:
 Q^=1;B[I:=int(input())]='OX'[Q];O|=1<<I;X,O=O,X;p(*B)
 if any(X&i==i for i in(448,56,7,292,146,73,84,273)):p('OX'[Q],'win');break
else:p('Tie')