#open() is used to open new file either for writing or reading 
#take 2 parameter first) file fath   2nd) mode eg w for writing and r for reading
f=open("funny.txt",'a') # w will overwrite 
f.write("\ni love java")
#if i change above text and run it will oerwrite it
f.close() #reclaimed all resource by os 

# will dispaly it once 
f=open("funny.txt",'r') 
print(f.read())
f.close()

#to print line by line use  for loop
f=open("funny.txt",'r')
for line in f:
    print(line)
f.close()

#want to count numb of word  in each line 
f=open("funny.txt",'r')
for line in f:
    token=line.split(' ')
    print(len(token))
f.close()

#to display line by splitting with space
f=open("funny.txt",'r')
for line in f:
    token=line.split(' ')
    print(str(token))
f.close()

#using with methoed no need to close the file 
with  open("funny.txt",'r') as f:
    print(f.read())

print(f.closed)#tell the file closed or not 

#__name__  is predifned var in python value is __main__ it entery point in py prog like c++ void main(){}
def cal(a,b):
    return a*b

if __name__=='__main__':
    area=cal(10,20)
    print("area=",area)