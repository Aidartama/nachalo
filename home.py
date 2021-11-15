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
'''
a=open('users.txt','w')
a.write(input('введите логин   :')+' '+input('введите пароль:  ')+\n)
a.close() 
'''
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
