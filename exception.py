#exception are the error detected at time of prog execution
x=int(input("enter numb="))
y=int(input("enter numb=")) #if enter zero  it will stop program here 
try:
    div=x/y
except Exception as e: #this is genral exception handle every exception 
    #specific exception occur as store in e 
    print("exception occured:",e)
    div=None
print("division=",div)

def cal(a,b):
    return a*b

print("area=",cal(2,5))
#handle specific exception there is no need to print e 
x=int(input("enter numb="))
y=int(input("enter numb="))
try:
    div=x/y
except ZeroDivisionError as e:
    print("divison by zero exception occured")
    div=None

print("division=",div)


#to hanlde multile exception str and div by zero
x=input("enter numb=") 
y=int(input("enter numb="))
try:
    div=x/y
except ZeroDivisionError as e:
    print("divison by zero exception occured")
    div=None
except TypeError as e:
    print("type error exception")
    div=None
print("division=",div)