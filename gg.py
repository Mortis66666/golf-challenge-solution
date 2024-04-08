p = 0

while 1:
	p |= 2<<int(input())+(p%2)*9
	print(bin(p>>10)[2:].rjust(9, "0"))
	print(bin(p&0b111111111)[2:-1].rjust(9, "0"))
	print(bin(p>>(p%2)*9+1)[2:-1].rjust(9, "0"))
	print(*["-"if(p&2**(i+9))+(b:=p&2**i)<1else"OX"[b>>i]for i in range(1,10)])
	if any(y==y&(p>>(p%2)*9+1)for y in[896,112,14,584,292,146,168,546]):print("XO"[p&1]+" win");break
	p ^= 1