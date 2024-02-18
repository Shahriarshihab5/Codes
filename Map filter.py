l=[1,2,5,7,8,9]
#map
newl=list(map(lambda x :x*x,l))
print(newl)

def any(a):
    return a>2
#Filter
newwl=list(filter(any,l))
print(newwl)

