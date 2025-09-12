def sum(num):
    e=0
    o=0
    for i in num :

        if i%2==0:
            e=e+i
        else:
            o=o+i
    return e,o
num=list(map(int,input("Enter numbers: ").split()))
e,o=sum(num)
print("Sum of even numbers: ",e)
print("Sum of odd numbers: ",o)
