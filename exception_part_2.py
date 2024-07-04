#raised standard(pre defined) exception 
try:
    raise MemoryError("memory error")
except MemoryError as e:
    print(e)
#can also use genric 
try:
    raise Exception("type error")
except Exception as e:
    print(e)

#user defined  exception
class Accident(Exception):
    def __init__(self, m) :
          self.msg=m
    def print_exception(self):
        print("user defined  exception=",self.msg)

try:
    raise Accident("acciden bet two motors")
except Accident as e:
    e.print_exception()

#finally key word
#if there are many exception you dont know use finally key word eg fucn have two exception handle just one will go ahead and show one exceptio
def proc_file():
    try:
        f=open("funny.txt",'r')
        x=15/0 #there is no handling for it like more other exception show exception but still go to finally statement
    except FileNotFoundError as e: #will handle just file not found 
        print(e) 
    finally:
        print("cleaning file")
        print("finally ")
    f.close()

 
proc_file()
