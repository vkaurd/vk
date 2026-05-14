'''
#1
s='suiii'
for i in s:
    print(i)

#2
s='abcdeabbc'
print(*set(s)) #* for str

#3
s1, s2 = set('juventus'), set('arsenal')
alp=set('abcdefghjiklmnopqrstuvwxyz')
print(s1^s2) #^ without and
print(s1-s2)
print(s2-s1)
print(alp-(s1|s2)) #| all

#4
l=[]
while True:
    n=int(input())
    if n == 0:
        break
    if n > 0:
        l.append(n)
    else:
        l.append(n*-1)
print(l)

#5
l=[1,2,3,4,5,6]
sumc=0
sumn=0
for i in range(len(l)):
    if i %2==0:
        sumc+=l[i]
    else:
        sumn+=l[i]
print(sumc/sumn)

#6
s=['arsenal', 'juve', 'http://arsenal.com', 'http://juve.com']
res=[]
for i in s:
    if i[:7]=='http://': #or we can use i.startswith('http://')
        res.append(i)
print(res)

#1
word=input()
score=0
scrabble={}
p1='aeioulnstrавеинорст'
p2='dgдклмпу'
p3='bcmpбгёья'
p4='fhvwyйы'
p5='kжзхцч'
p8='jxшэю'
p10='qzфщъ'
p=[(p1,1),(p2,2),(p3,3),(p4,4),(p5,5),(p8,8),(p10,10)]
for latters, price in p:
    for l in latters:
        scrabble[l]=price
for l in word:
    score += scrabble[l]
print(score)

#2
data=[('cat1', 7, "bro1", "bobrov1"), ('cat55', 7, "bro1", "bobrov35"), ('cat99', 77, "bro1", "bobrov1"),('cat2', 33, "bro2", "bobrov2"), ('cat3', 1, "bro3", "bobrov3"), ('cat4', 11, "bro4", "bobrov4")]
res={} #slovar
for cat, age, name, surname in data:
    fio=name+' '+surname
    info=cat+', '+str(age)
    if fio not in res:
        res[fio] = info  #just name and cat
    else:
        res[fio] = res[fio]+', '+info #показываем куда вписать another one кота
print(res)

#3
import random
import time 
size=[10,100,1000,10000]
for s in size:
    nums=[random.randint(1,100) for i in range(s)]
    start = time.time()
    for i in range(len(nums)):  #again
        for j in range(len(nums)-1): #9 пар, 10 чисел, left to right
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    end = time.time()
    res=end-start
    print(s, res)
'''
#4
import random
win=[7,6,5,4,3,2,1]
rings=[]
temp=[7,6,5,4,3,2,1]
while len(temp)>0:
    ind = random.randint(0, len(temp)-1)
    v=temp.pop(ind)  #ind in v
    rings.append(v)
tower = [rings, [], []]
while True:
    print('colishki:', tower)
    s=int(input()) #colisko
    e=int(input())
    ring = tower[s].pop() # minus last one ring
    tower[e].append(ring)
    if tower[0]==win or tower[1]==win or tower[2]==win:
        print('oh my god, u did it')
        break

