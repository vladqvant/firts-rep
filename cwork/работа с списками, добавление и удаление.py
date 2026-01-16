spisok = ['Jenya', 'Sanchoz', 'Jora']
#massage0 = f'invite brakfest,{spisok[0]}' 
#massage1 = f'invite brakfest,{spisok[1]}' 
#massage2 = f'invite brakfest,{spisok[2]}' 
#print(massage0)
#print(massage1)
#print(massage2)
#rem_gost = spisok.pop(0)
#print(rem_gost)
spisok[0] = 'Dasha'
#print(spisok)
#new_massage0 = f'invite {spisok[0]}'
#new_massage1 = f'invite {spisok[1]}'
#new_massage2 = f'invite {spisok[2]}'
#print(new_massage0)
#print(new_massage1)
#print(new_massage2)
spisok.insert(0, 'Vachik')
spisok.insert(2, 'Babyshka')
spisok.append('Roma')
print(spisok)
bad_news = 'Приглашается всего два гостя'
print(bad_news)
pop1 = spisok.pop(0)
pop2 = spisok.pop(0)
pop3 = spisok.pop(0)
pop5 = spisok.pop(0)
print(spisok)
mas_j = f'invitation {spisok[0]}'
mas_r = f'invitation {spisok[1]}'
print(mas_j)
print(mas_r)
lot = len(spisok)
b = f'Количество гостей', lot
print(b)

del spisok[0]
del spisok[0]
print(spisok)

