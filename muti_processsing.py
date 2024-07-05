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

if __name__=="__main__":
  arr=[2,5,6,7]
  p1=multiprocessing.Process(target=cal_square,args=(arr,))
  p2=multiprocessing.Process(target=cal_cube,args=(arr,))
  p1.start()
  p2.start()

  p1.join()
  p2.join()

  print("done")