#3 INITIALISE A LIST CONTAINING ALL ENGLISH ALPHABETS
'''
l = [];

for i in range(65,91):
    l.append(chr(i))
for i in range(97,122):
    l.append(chr(i))
    
print(l)
'''

l=[0,1,2,3,4,5,6,7,8,9,10,11,12]
'''
print(l[::4])

print(type(l))

m=[0,2,1,1,1,2]
p=[]
b=['s','t','u']
p=b+[5]+['5'];
print(m[0]+m[3])
print(p)

for x in range(1,4):
    b+=['lol'];
    print(b)
    
'''
h=[]
l.pop(1);
print(l)
del l[::2]
print(l)

s=[[]] * 2
s[1].append(0)

print(s)

u=[8 for i in range(9)]
print(u)
p=[1,2,3,4,5]
print(p[2]*3)

a='hellooooooo'
print(a[2:4])
print(a[::-1])

print(p[::-1])

print(p*2)
#print(p*2.0) error

q=[7,7,7,7]

p.append('0')
print(p)

#print(p+5)

t=['lol']
t+='hehe'
t+=[223]
#t=t+'haha'
print(t)
print(' '.join(['morning','evening']))

x=range(10)
z=range(20)
#y=range(11:15)
print(x)

for i in range(5,9):
    print(i)

x=[0,1,[2]]
print(x[2][0])
































