#1
n=float(input())
if n > 0:
    print('+')
elif n <0:
    print('-')
else:
    print('0')

#2
n=float(input())
while n !=0:
    if n > 0:
        print('+')
    elif n <0:
        print('-')
    break

#3
for i in range(1,51):
    if i%2==0:
        print(i*2)
    else:
        print(i/3)

#4
import random
t = random.randint(1,101)
a=10
for i in range(a):
    pop = int(input())
    if pop ==t:
        print('suii')
    elif pop > t:
        print('less')
        a-=1
    else:
        print('more')
        a-=1
if a == 0:
    print('lmao, u lose')
    print(t)

#5
s=input()
for z in '+-*/':
    if z in s:
        zn = z
        break
pos = s.find(zn)
a=int(s[:pos])
b=int(s[pos+1:])
if zn == '+':
    print(a+b)
elif zn == '-':
    print(a-b)
elif zn == '*':
    print(a*b)
elif zn == '/':
    if b!=0:
        print(a/b)
    else:
        print('no no no!')

#6
for i in range(14):
    if i ==0 or i ==12:
        print('*'*7)
    elif i == 2 or i==10:
        print(' '+'*'+' '*3 +'*')
    elif i == 4 or i == 8:
        print(' '*2+'*'+' '+'*')
    elif i==6:
        print(' ' *3 + '*' + ' ' *3)

#7
a=int(input())
b=int(input())
d=0
for i in range(a,b+1):
    for j in range(1,i):
        if i % j == 0:
            d+=1
    if d == 1:
        print(i)
    d=0

#8
x=int(input())
p=int(input())
y=int(input())
years=0
while x<=y:
    x=int(x*(1+p/100))
    years+=1
print(years)

#9
s=input()
m1=0
m2=0
for i in s:
    n=int(i)
    if n == 0:
        break
    if n > m1:
        m2=m1
        m1=n
    elif n>m2 and n!= m1:
        m2=n
print(m2)

#10
n= int(input())
a=1
for i in range(1, n+1):
    a*=i
print(a)

#11
n=int(input())
a=0
b=1
for i in range(n-1):
    s=a+b
    a=b
    b=s
print(b)
