#coding:utf-8

l=("km","m","cm")
(n,s)=map(str,raw_input().split())

if 1<= int(n) <=1000:
	
	if s==l[0]:
		a=int(n)*1000*100*10
		print a
		
	if s==l[1]:
		a=int(n)*100*10
		print a
	if s==l[2]:
		a=int(n)*10
		print a
