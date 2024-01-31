a = int(input()) 
b = set(map(int, input().split()))  

e = int(input())  
r = set(map(int, input().split()))  

u = b.symmetric_difference(r) 
print(len(u))  