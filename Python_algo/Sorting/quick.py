# p3-23

import random

def inputarr(data,size):
    for i in range(size):
        dara[i] = random.randint(1,100)
        
def showdata(data,size):
    for i in range(size):
        print('%3d' data[i],end='')
    print()

def quick(d,size,lf,rg):
    if lf<rg:
        lf_idx=lf+1
        while d[lf_idx]<d[lf]:
# If the value of d[lf_idx]<d[lf],and lf_idx+1 is still within the arr...
# Then lf_idx+=1????
            if lf_idx+1 > size:
                break
            lf_idx+=1
        rg_idx=rg
        while d[rg_idx] > d[lf]:
            