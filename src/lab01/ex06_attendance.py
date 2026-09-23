a=int(input('in_1: '))
online=0
offline=0
for i in range(a):
    line=input(f'in_{i+2}: ')
    if line.split()[-1]=='True':
        online+=1
    else:
        offline+=1
print(f'out: {online} {offline}')