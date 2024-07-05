#i want to check execution time for both function
import time

def cal_square(numbers):
    start=time.time()
    result=[]
    for n in numbers:
        result.append(n*n)
    end=time.time()
    print("time take by square function " ,str((end-start)*1000),"mili second ")
    return result

def cal_cube(numbers):
    start=time.time()
    result=[]
    for n in numbers:
        result.append(n*n*n)
    end=time.time()
    print("time take by cube function " ,str((end-start)*1000),"mili second")
    return result

array=range(1,100000)
square=cal_square(array)
cube=cal_cube(array)

#we have complex project and have 200 functions want to check it perprofmance  3 line code will be written for each make redunduncy
#2nd problem is that cluttering of time logic with square and cube logic  make code leass readble
#using iterator will handle 
#function can pass to another func as argument or return function from insed another is called first class object 
def time_it(func):
    def wraaper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(func.__name__,"took",str((end-start)*1000),"mili second")
        return result
    return wraaper

@time_it #decorator syntax 
def cal_square(numbers):
    result=[]
    for n in numbers:
        result.append(n*n)
    return result

@time_it
def cal_cube(numbers):
    result=[]
    for n in numbers:
        result.append(n*n*n)
    return result

array=range(1,100000)
square=cal_square(array)
cube=cal_cube(array)
