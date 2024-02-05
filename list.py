li=[1,2,3]
print(type(li))
print(li)
print(li[1])

#Add in list
hablu=[4,6,7,8]

hablu.append(100)
print(hablu)
#insert
hablu.insert(0,333)
print(hablu)
Remove
hablu.remove(7)
print(hablu)
#pop
hab=[5,4,7,8,9,99,63]
hab.pop(3)
print(hab)

#del
del hab[2]
print(hab)

#clear
hab.clear()
print(hab)

#listComprehension

for s in num:
    print(s*2)
num =[1,2,3,4,5]
Double=[w+4 for w in num]
# print(Double)

#sort List Item
number=[3,2,7,4,0,6]
char=['b','d','f','n','a','e']
number.sort()
char.sort()

print(number)

print(char)

#ReverseList

Num = [1,2,3,4,5,6]
Num.sort(reverse =True)
print(Num)
#Copy List
number =[1,2,3,4,5,6,7,8,9]
num2=number.copy()
print(num2)
print(number)
num1=[1,2,3,4,5]
num2=[6,7,8,9,10]
num3=num1+num2
print(num3)
num1.extend(num2)
print(num1)