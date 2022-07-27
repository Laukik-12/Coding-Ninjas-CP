'''Check Armstrong'''
n = int(input())
def powerof(n):
    sum = 0
    temp = n
    while(temp>0):
        temp=temp//10
        sum=sum+1
    return sum
def number(n):
    a = powerof(n)
    temp = n
    b = 0
    while(temp>0):
        b = b+(temp%10)**a
        temp = temp//10
    return b


c = number(n)
if(n==c):
    print("true")
else:
    print("false")
