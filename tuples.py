'''
a=['Aidar','dastan','nestan','shabdan']
b='malik'
print(b.join(a))


imena=['Aidar','dastan','nestan','shabdan']
gody=(2003,2005,2012,2009)
print(imena.append(gody))
print(imena)


names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',
	 'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack',
	 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy',
	 'Jack', 'Jackson', 'Jhon',]
print(names.remove('Jack'))
print(names)



Im=[]
imy='Aidar'
god=2003
yzyk='python'
Im.append(imy)
Im.append(god)
Im.append(yzyk)
print(Im)



pythonList = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]
pythonList.index('loop')
pythonList.pop(6)
print(pythonList)



numbers = [0,2,4,7,1,8,0,3,7,0,-2,4,0,0,-1,7,-43,0,8,-3,6,9]
print(sum(numbers)*len(numbers))



a=['Lamborgini',17,'4456',2020,'Paris','USA',11,23]
numbers=[]
letters=[]
b=a.index('Lamborgini')
letters.append(a[0])

b=a.index('USA')
letters.append(a[5])

b=a.index('Paris')
letters.append(a[4])

c=a.index(17)
numbers.append(a[1])

c=a.index(2020)
numbers.append(a[3])

c=a.index(11)
numbers.append(a[6])

c=a.index(23)
numbers.append(a[7])

print(numbers,letters)





numbers = [0,2,4,7,1,8,0,3,7,0,-2,4,0,0,-1,7,-43,0,8,-3,6,9]
print(numbers[1:3])
'''
