# p3-16

data=[16,25,39,27,12,8,45,63]
print('Bubble sort, original data:')
for i in range(8):
    print('%3d' %data[i],end='')
print()

for i in range(7,-1,-1):
    for j in range(i):
        if data[j]>data[j+1]:
            data[j],data[j+1]=data[j+1],data[j]
    print('The %d th list is:' %(8-i),end='')
    
    for j in range(8):
        print('%3d' %data[j],end='')
    print()
    
print('The result is:')
for j in range(8):
    print('%3d' %data[j],end='')
print()