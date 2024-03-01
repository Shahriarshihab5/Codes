def factorial(a):
  sum=0
  fact = 1
  if a==1:
    pass
  else:
      for i in range(0,a):

              fact = fact* a
              a=a-1


  return fact

def sum_fact(b):
    sum=0
    factorial(b)
    for j in range(0,b):

        sum=sum+factorial(b)
        b=b-1
    print(sum)



n=int(input())

sum_fact(n)
