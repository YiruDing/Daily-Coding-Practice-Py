# p3-12

SIZE=8
def showdata(data):
    for i in range(SIZE):
        print('%3d' %data[i],end='')
    print()
    
def insert(data):
    for i in range(1,SIZE):
        tmp=data[i]
        no=i-1
        while no>=0 and tmp<data[no]:
            data[no+1]=data[no]
            # tmp<data[no] means 
            # if the value of data[i] is less then the value of data[i-1]
            # data[i]=the value of data[i-1]
            # reassign the value
            no-=1
            # take one step back and 
            data[no+1]=tmp
            # data[i-1]=the value of data[i]
            # store  the less value

def main():            
    data=[16,25,39,27,12,8,45,63]
    print('The original list:')
    showdata(data)
    inserdata(data)
    print('The result list is:')
    showdata(data)
    
main()
