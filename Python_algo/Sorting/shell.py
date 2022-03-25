# p3-15

SIZE=8

def showdata(data):
    for i in range(SIZE):
        print('%3d' %data[i], end='')
    print()
    
def shell(data,size):
    k=1
    jmp=size//2
# python//表示取整除 ，返回商的整数部分（向下取整）
    while jmp !=0:
        for i in range(jmp,size):
            tmp=data[i]
            j=i-jmp
            while tmp<data[j] and j>=0:
                data[j+jmp] = data[j]
                # data[i]= data[j]
                j=j-jmp
                data[jmp+j]=tmp
                # data[j]= tmp(the value of the original data[i])
        print('The %3d th list:' %k,end='')
        k+=1
        showdata(data)
        print('------------------------------------------')
        jmp=jmp//2
         
def main():
    data=[16,25,39,27,12,8,45,63]
    print('The original list is : ')
    showdata(data)
    print('----------------------------------------------')
    shell(data,SIZE)
    
main()