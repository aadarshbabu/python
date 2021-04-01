# # dictonary is also a mutable data type...
# #it store a data in key value pair

# dic= {"aadarsh":111,'raj':333,'suman':"raj","Bool":True,"suman":"sonu"}
# dicte= dict() #it is way to create the dictinory...
# dicte["aadarsh"]=33 # assign the value in dictonary...
# dicte["raj"]=44 # assign the value in dictonary...
# dicte["raj"]=44 # it cant contain the dublicate value. in spasific key.
# dicte["raj"]=445 # if you change the value dictonary will replace the value...
# dicte["baj"]=445 # if you change the value dictonary will replace the value...
# print(dicte)
#     # you can crate the value..\


# no_of_value= input("how many value enter you a dictonay")
# dis={} 
# key = input("enput the key")
# value = int(input("input the vlaue")) # input function is always take a string .. if you get the interge value first type cast the string to int. above this method...
# dis[key]=value
# print(dis)

# print(dic)
# print(dic.keys()) # extract the key in dictonary..
# print(dic.values()) # extract the value in dictonary..

# temp=dic.copy() #its copy the dictonary....
# print(temp)

# print(dic.popitem()) # is pop last element..
# print(dic.pop('aadarsh')) # its pop value in given key

# temp=dic.pop("aadarsh")# value also remove the dictonary
# print(temp)
# dictt= {"sol":33,"ram":555}
# dic.update(dictt)# this function is appent ont dictonary to another dictonary.
# # you only pass the update function to another dictornary..
# dic.update({"hello":333})
# print(dic)

# #adding the new value...
# dic["hello"]=330
# print(dic)

# #update the values
# dic['aadarsh']=44
# print(dic)

# print(dic.clear()) # clear the dictonary
# print(dic)
# dic.setdefault("helo",4) # set the defult value in dictonary..
# print(dic)
