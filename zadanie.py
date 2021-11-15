'''
a=0
for i in range(1,1000):
	if i%3==0 or i%5==0:
		a+=i
print(a)


b=0
for i in "4729461084":
	b+=int(i)
print(b)

'''
'''
b={'god': input('vvedi god'),
'месяц': input('vvedi month'),
'day': input('vvedi day')}
print(b)

'''
'''
a=input('год')
f=input('месяц')
c=input('день')
d={'year':{a},
'month':{f},
'day':{c}}
for value in d.items():
	print(f'{a}-{f}-{c}')

'''
'''
a=('1'+'1'+'2'+'3'+'4')
print(len(a))


a = '1'
b= int(a)*7
print(b)


mkdir -p/home/admins/рабочий\стол/LINUX/Aidar


a=17531//3 
if a>=5821:
	print(a,'a>=5831')
elif a<=5821:
	print('5821')



a=4292/5
if a<=3:
	print(a/3)
else:
	print(a)
'''
a=int(input('вес:    '))
b=int(input('рост:   '))
d={'вес':{a},
'рост':{b}}
if a>=80 and b<=170:
	print('не ешьте вообше')
elif a<=60 and b>=170:
	print('скоро умреш)')
