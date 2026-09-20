a=input('ФИО: ')
initials=''
k=0
for i in (a.split()):
    initials+=i[0]
for n in (a.replace(' ','')):
    k+=1
print(initials,k)