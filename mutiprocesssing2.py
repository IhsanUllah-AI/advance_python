#muti processsing
import multiprocessing
square_result=[]
def cal_square(numb):
    print ("square of multi  give number")
    for x in numb:
       print("square=",x*x)
       square_result.append(x*x)
    print("suare function result=",square_result )

if __name__=="__main__":
  arr=[2,5,6,7]
  p1=multiprocessing.Process(target=cal_square,args=(arr,))
  p1.start()
  p1.join()
  print("suare result=",square_result )#this will give empty list even suare is calcalulated why
  #beacuase each process has its own address space and program dont share var with another process to share it use itercommunication teachinique
  #here has two process square and main square_result has global var but in square has its own adress space not share with main
  #if i want to display must print in square 