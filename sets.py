# a set contains unique values
'''
s={'s','p','a','m'}
print(s)#prints un ordered , if printed multiple times, preints same order

x=set('abcde')
p=set('he is a fool') #print unique elements onlyyyyyyyyy
print(p)

l=set([1,2,3,4,4,4]) #list in set
print(l)

l.add(5)
l.add('5')
l.add(5)
print(l)

s1={1,2,3,4}
s2={-5,-6,7,8}
#s1.add(s2)
ls=[-5,'6t']
#s1.add(set(ls))
s1.update(s2)
print(s1)
s2.update(ls)
print(s2)
s2.update(s1,ls)
print(s2)

#sets are mutable

print(s1|s2)#union
print(s1&s2)#intersection
print(s1-s2)#values in s1 but not in s2'''

#remove(), discard() -> go and do it ie no error msg


bas={'app','orr','app','pea','orr','ban'}

print(bas)
