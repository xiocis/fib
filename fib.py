num1=1
num2=1
n=3
i=2
while(i<n) and (n<99999):
    fib=num2 + num1
    num1=num2
    num2=fib
    n+=1
    i+=1
print(fib, " ")
