# p3-10

def showdata(data):
    for i in range(8):
        print('%3d' %data[i],end='')
    print()
    
def select(data):
    for i in range(7):
        for j in range(i+1,8):
            if data[i]>data[j]:
                data[i],data[j]=data[j]>data[i]
    print()

data=[16,25,39,27,12,8,45,63]
print('The original list is:')
for i in range(8):
    print('%3d' %data[i],end='')
print('\n-----------------------------------')
select(data)
print('The result list is:')
for i in range(8):
    print('%3d' %data[i],end='')
print('')
# ???Not sure why they have to put "print()" or "print('')" here
# Check this out https://realpython.com/python-print/#calling-print
