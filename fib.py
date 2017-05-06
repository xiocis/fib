##var's
num1=1
num2=1
q = True
##while
while (q==True):
    print("Значение какого элемента ряда \
Фибоначчи вы хотите узнать?")
    n=int(input("Ввод - ")) 
    i=2
    if (n==1):
        q=False
    if (n!=1):
        while (i<n):
            fib=num2+num1
            num1=num2
            num2=fib
            i+=1
    print(fib)
    print("Введите 1 для выхода из цикла")
