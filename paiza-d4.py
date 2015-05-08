#coding:utf-8

m=input("")
l=[]

if 1<= m <=20:
	for n in range(0,m):
		h=raw_input("")
		l.append(h)
	
print "Hello "+",".join (l)+"."
