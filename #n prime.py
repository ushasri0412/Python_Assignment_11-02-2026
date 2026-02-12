#n prime 
def first_n_primes(n):
    num = 2
    found = 0
    while found < n:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
            found += 1

        num += 1
n = int(input("Enter N: "))
first_n_primes(n)
