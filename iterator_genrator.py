x=300 #this is global avrible definde outside function
def myf():
    global x #thuis is definde inside but keyword global use so this is also global so these two are same result will print 200 for both
    x=200
    print(x)
myf()
print(x)
#in this case 
y=300 #gloval used any any where
def my():
    y=200 #scope varaible used only insid function
    print(y)
my()
print(y)
#scope var can be used function within function
def mar():
    m=400
    def mal():
        print("my marks =",m)
    mal()
mar()
#iterator is an object which is contable number of values eg tuple
#iterable used two function iter() and next()
boy=("ihsan","wisal","ali","asad","ijaz")
#looping through in iterator
#iteartae the value of tuple
for x in boy:
    print(x)
#iterate the value of string
x="luhna fayaz"
for y in x:
    print(y)
#iterate tuple through function not with loop
z=iter(boy)
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
#itaertor strin through function'
w="Ihsan Ullah Khan"
n=iter(w)
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))

#used --iter--() func and next and dispaly value from 1 upto 5 use in class
class num:
    def __iter__(self):
        self.s=1
        return self
    def __next__(self):
        x=self.s
        self.s +=1
        return x
ob=num() #creation of object
x=iter(ob)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
#this will not stop on 5 write other line it will go ahead 
#now we want o stop on 10  for loop did stopn on particular value then we used iteration
class num:
    def __iter__(self):
        self.s=1
        return self
    def __next__(self):
        if self.s<=20:
            x=self.s
            self.s+=1
            return x
        else:
            raise StopIteration
ob=num()
x=iter(ob)
for x in x:
    print(x)

       
ob=num() #creation of object
x=iter(ob)
print("to dispaly even number upto 20")
class even:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        self.a+=1
        if self.a%2==0:
            if self.a<=20:
                 x=self.a
            else:
                raise StopIteration
            return x
ob=even()
x=iter(ob)
for x in x:
    print(x)


class remoteControl:
    def __init__(self):
        self.channel=['geo','ary','24','bbc','cnn','92','samma']
        self.index=-1        
    def __iter__(self):
        return self
    def __next__(self):
        self.index +=1
        if self.index==len(self.channel):
            raise StopIteration
        return self.channel[self.index]
   
#for loop dont work in iterator
obj=remoteControl()
it=iter(obj)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

#genrator is simply way to create iterator
#for loop work in genrator 
#genrator used yeild
def remote_control_next():
    yield "ary"
    yield "geo"
    yield "24"
    yield "bbc"

itr=remote_control_next()
print(next(itr))
print('genrsator output')
for x in remote_control_next():
    print(x)

#use genrsator to create fib series
def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

for x in fib():
    if x>40:
        break
    print(x)