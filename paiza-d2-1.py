#coding:utf-8

(a,b)=map(int,raw_input().split())

if 0<=a<=1000 and 0<=b<=1000:
	if a==b:
		print "eq"
		
	elif a>=b:
		print a
		
	else:
		print b
	
