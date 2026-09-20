from string import *
alf=ascii_uppercase
d=digits
a=input('in: ')

start_index=-1
second_index=-1

out=''
for i in range(len(a)):
    if a[i] in alf:
        start_index=i
        break
for i in range(len(a)):
    if a[i] in d:
        second_index=i+1
        break
difference=second_index-start_index

for i in range(start_index,len(a),difference):
    out+=a[i]
    if a[i]=='.':
        break
print(f'out: {out}')