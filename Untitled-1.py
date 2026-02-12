def palindrome(num):
    number = num
    rev = 0
    while num>0:
        digit=num % 10
        rev=rev*10+digit
        num=num//10
    if number==rev:
        return "Yes"
    else:
        return "No"


n = int(input("Enter a number: "))   # convert to int
print(palindrome(n))
