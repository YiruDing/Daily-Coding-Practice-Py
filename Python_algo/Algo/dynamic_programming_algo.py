# p1-19

output = [None]*1000
def Fibonacci(n):
    result=output[n]
    
    if result==None:
        if n==0:
            result=0
        elif n ==1:
            result=1
        else:
            result= Fibonacci(n-1) + Fibonacci(n-2)
        output[n] = result
    return result