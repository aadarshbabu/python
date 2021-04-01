i=0
while i<29:
    print(i)
    i=i+1

loop in list...
i=0
lis=['mango','gwave','apple','papaya','banana'] #i itrate in 0 1 2 3 and so on..
                                                #name itrate in list value..
for i,name in enumerate(lis):
    print(i,lis[i])     # its print the list[0,1,2,3]  elements.
    print(i,name)         # all the statemnet are valid...
    print(name)
for i in range(0,len(lis)):
    print(i,lis[i])
     range base loop value one by one copy the i elemnet and then every etration new value get assign in i
     print(type(i))

loop in tuple
tup= "aadarsh","singh",True,False,(11,12,"a","C"),"raj"
for element in tup:
    print(element)

    #print the odd number in 1 to 20 in for loop   question..
for i in range(0,40,2):  # 42 is exculaded in range thatsway. loop is itrate in 38
    print(i)

# range funcion in create the this type of list...
for i in [11,22,12,3,4,5,3,23,2,4]:
    print(i)
   
        


    #loop in dictonary
dic= {"aadarsh":111,'raj':333,'suman':"raj","Bool":True,"suman":"sonu"}
for element in dic:
    print(element)


while loops
i=0
print(type(i))
while i<len(tup):
    print(tup[i])
  
    i+=1

