print('введите фамилию')
fam = input()
print('введите имя')
name = input()
print('введите дату рождения')
date = input()
print(fam, name, date, sep='_')
x = fam
fam = name
name = x
print(fam, name, int(date)+60, sep='_')
