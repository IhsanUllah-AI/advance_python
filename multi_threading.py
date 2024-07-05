import multiprocessing.process
import time
import threading
def cal_square(numb):
    print ("square of  give number")
    for x in numb:
       time.sleep(0.2)
       print("square=",x*x)

def cal_cube(numb):
    print("cube of given number")
    for n in numb:
        time.sleep(0.2)
        print("cube=",n*n*n)


start=time.time()
arr=[2,3,4,5]
t1=threading.Thread(target=cal_square,args=(arr,))
t2=threading.Thread(target=cal_cube,args=(arr,))
t1.start()
t2.start()
t1.join()
t2.join()

print("done in ",time.time()-start)


#muti processsing
import multiprocessing

def cal_square(numb):
    print ("square of multi  give number")
    for x in numb:
       print("square=",x*x)

def cal_cube(numb):
    print("cube of given number")
    for n in numb:
        print("cube=",n*n*n)


arr=[2,5,6,7]
p1=multiprocessing.Process(target=cal_square,args=(arr,))
p2=multiprocessing.Process(target=cal_cube,args=(arr,))
p1.start()
p2.start()

p1.join()
p2.join()

print("done")
