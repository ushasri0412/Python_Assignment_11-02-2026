#import re
#print(re.search(r"ab*","a"))
#print(re.search(r"ab+","abbb"))
#print(re.search(r"colou?r","color"))
#print(re.search(r"\d{4}","Year 2025"))
#print(re.search(r"\d{2,4}","ID: 123"))# matches 2 to 4 digits (12,123,1234) n=min , m =max

def add():
    a=input()
    b=input()
    print(a+b)
add()

def welcome(name):
    print("welcome",name)
welcome("Usha")