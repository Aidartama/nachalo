import f
print(f)










'''
a=[1,1,2,3,5,8,13,21,34,55,89]
b=[1,2,3,4,5,6,7,8,9,10,11,12,13]
for elem in a:
	if elem==b:
		print(elem)
	else:
		print('нет')





'''





















'''
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
a={'besh_barmak':130}
menu.update(a)
menu.update({'lagman':135})
menu.update({'borsh':"повар отвратительно готовит,поэтому убрали"})
print(menu)


menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
a={'drinks': {'Coca-cola','Sprite',"Fanta"}}
menu.update(a)
print(menu)

file = open('a.txt', 'w')
file.write(' ')

a=open('users.txt','w')
a.write(input('введите логин   :')+' '+input('введите пароль:  ')+\n)
a.close() 

with open('users.txt','r')as f:
	a= f.read()
	if 'w'in i:


a = open('python.txt','r')
b = (a.read().split())
t_words=[]
for i in b:
	if 't' in i or "T" in i:
		t_words.append(i)
print(t_words)

'''

'''
text = В 1960-е годы в СССР начались попытки запускать аппараты к Венере в рамках космической программы «Венера».
Первый пуск был неудачными, но уже второй аппарат Венера-1 достиг зоны действия тяготения планеты,
где с ним было потеряна Венера связь — он пролетел на расстоянии Венера 100 000 км от поверхности.
В 1965 году результат был уже лучше — 24 000 км.
Венера-4 Венера доставила Венера спускаемый аппарат и смогла Венера получить данные о давлении,
что использовали при построении следующих аппаратов.
Венера-7 впервые совершила мягкую посадку Венера на другую планету — в 1970-м году.
 Венера-9 в 1975 году впервые передала телевизионную панораму с Венеры на Землю.
text.split(" ")
q=0
for i in text:
	if i=="Венера":
		q+=i
print(q.len())
	break

a=[1,1,2,3,5,8,13,21,34,55,89]
for elem in a:
	if elem<5:
		print(elem)
'''
