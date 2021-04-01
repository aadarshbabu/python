 #list is always mutable data sturectue....


lis=['hello',43,434,True,False,2.5j,44.0]
print(type(lis))
print(lis)
 # You can append the data into a list...

lis.append('hello')
print(lis)
lis.append("sonu")
print(lis)
lis.pop()
print(lis)
print(lis.count("hello"))
liste=['hello','world','world']
liste.insert(2,"hello")
liste.sort() #sort method is always work on same value in the list..
print(liste)

# print(liste*3)#you also print multiple type in list

print(lis+liste) #concatinate the liste

lis.clear()
print(lis)
lis.remove(43)
print(lis)



# appdend your list.. data
# way to insert you data.. itrative.. way..
table=[]
for i in range (0,22,2):
    table.append(i)
print(table)



# you can also insert the data

liste=[33,55,23,553,4]
liste+=[554]  #  you and also appent the data..
print(liste)


tup=55,43,5,43,4
print(type(tup))

l1=list(tup) # you can convert the tupel to list.. 
print(l1)

t1=tuple(l1) # also convet the list to tuple..
print(t1)



# if you convert the data into the dictonary to list or tuple only key is appent in list and tupel

dic= {"aadarsh":111,'raj':333,'suman':"raj","Bool":True}
l2= list(dic)
l3= tuple(dic)
print(l2)
print(l3)