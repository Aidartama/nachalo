a=input('введите имя:   ')
b=int(input('возраст:   '))
c=input('какие языки вы знаете из перечисленных?python,java,javascript:   ')
ls='вы прошли'
fs='вы прошли'
d=['python']
k=['java']
f=['javascript']
if b>=18 and b<=60:
	print(ls)
elif c==d or c==k or c==f:
	print(fs)
elif ls==fs:
	print('вы прошли')
else:
	print('извините',[a],'вы не подходите!')
