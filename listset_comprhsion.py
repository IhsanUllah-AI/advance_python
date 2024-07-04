#comprehinsion mean transfrom list to another form
array=[1,2,3,4,5,6,7,8,9]
#want to find even list
even=[]
for i in array:
    if i%2==0:
        even.append(i)
print(even)
#this is 4 step process using comprehinson will do it in one step
even=[ i for i in array if i%2==0]
print(even)
srt=[i*i for i in array ]
print(srt)
mul_2=[i*2 for i in array]
print(mul_2)

#set comprehinsion as same as list use braces instead of bracket
#set unordered,unindexed unchangebkle
a=set([1,2,2,3,4,5,6,7,4,3])
print(a)
even={i for i in a if i%2==0}
print(even)
sqrt={i*i for i in a}
print(sqrt)

#dict comprehinson
cities=["isalmab",'delhi','colombo','new rok']
contires=['pak','ind','sri','usa']
d=zip(cities,contires) #combine two list
print(d) #will give object 
for a in d:
    print(a)  #will give tuple 
dic={city:country for city,country in zip(cities,contires)}
print(dic)