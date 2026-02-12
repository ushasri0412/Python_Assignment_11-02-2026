def prime(n):
    if n<= 1:
        return "Not Prime"
    i=2
    while i<n:
        if n%i==0:
            return "Not Prime"
        i+=1
    return "Prime"
num = int(input("Enter a number: "))
print(prime(num))
## def is_prime(val):
##       if val <=1: return false
##      for i in range(2,val ) or (2,val// 2+1):
##              if val % i =0: return false 
##      return true 

##def generate(n):
##  count=0
##  num=2
##  while count<=n:
##      if is_prime(num):
##          print(num,end=' ')
##          count+=1
##      num+=1
##n=10
##generate(n)