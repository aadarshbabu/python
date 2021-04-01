#tuple is non mutable data sructure in python.....


weeks=('sunday','monday','tuesday','thuresday','friday','saturday')
weeks='sunday','monday','tuesday','thuresday','friday','saturday'
#round bracessen in not mandatry.... in this tuple..
print(type(weeks))s
weeks.append("holiday") # you cant append a any data. in the tuple
print(weeks)

#Split also support in tuple

print(weeks[1:])
print(weeks[:5])
print(weeks[:-4])
print(weeks[-4:-1])


# you can concatiname the two tupes

tup= "aadarsh","singh",True,False,(11,12,"a","C"),"raj" #You can put tuple inside tuple..
result=weeks+tup # when you concatiante the two tuple it's always return a tuple 
print(type(result))  #concatinate the method...
print(len(tup)+len(weeks))
newtup=(12,444,23,4,5,5,23,434,5,1,5,7,555,)
print(min(newtup)) #min and max function is always work on a sime type of data sotre in tupel not for diffrent type of data..

# you can print multiple time in tupe data
# like
print(weeks*3)






# functions in tupel



# loop in tupels.......

for(day in weeks)
    print(day)