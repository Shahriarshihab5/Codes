myset = {1,False,"string"} #set e same jinish duibar hbena.thakle kate dibe
(print(myset))
print(type(myset))
print(len(myset))
u={1,2,3,4,5,6}
print(len(u))
#access set items
setitem={1,2,3,4,5,7,8,9}
for i in setitem:
    print(i)
print(3 in setitem)
#add
setitem.add(55)
set1={133,4423,5342,5424}

print(setitem)
setitem.update(set1)
(print(setitem))
#Remove
#item remove korar na thakleu error dibe
newset={1,4,5,6,5,0,8}
print(newset)
newset.remove(4)
print(newset)
#discard method
#item discard korar na thakleu error dibe na
newset.discard(3)
print(newset)

newset.remove()
print(newset)
Loop in set
loopset={"HAB","SHI","SHAH","SYED"}
for i in loopset :
 print(i)
 #join set item
set1={"A","b","C"}
set2={1,2,3}
set3=set1.union(set2)
print(set3)
set4={11,31,44,46}
set6={"AA","BB","CC"}
set6.update(set4)
print(set6)