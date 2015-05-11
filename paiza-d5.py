#coding:utf-8

# Ql@(m, n, o, p) = map(int, raw_input().split())

l=[]
(m, n) = map(int, raw_input().split())

if 1 <= m <=100:
	
	if 1 <= n <=100:
		
		for x in range(0,10):
			l.append(m)
			m+=n
						
print " ".join([str(t) for t in l])
