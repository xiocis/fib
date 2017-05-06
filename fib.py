import time

num1=1
num2=1
n=3
i=2
while(i<n):
    fib=num2+num1
    num1=num2
    num2=fib
    n+=1
    i+=1
    time.sleep(0.5)
    print(fib, " ")
