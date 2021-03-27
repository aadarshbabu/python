# dictonary is also a mutable data type...
#it store a data in key value pair

dic= {"aadarsh":111,'raj':333,'suman':"raj","Bool":True,"suman":"sonu"}
# print(dic)
# print(dic.keys()) # extract the key in dictonary..
# print(dic.values()) # extract the value in dictonary..

# temp=dic.copy() #its copy the dictonary....
# print(temp)

# print(dic.popitem()) # is pop last element..
# # print(dic.pop('aadarsh')) # its pop value in given key

# temp=dic.pop("aadarsh")# value also remove the dictonary
# print(temp)
dictt= {"sol":33,"ram":555}
# dic.update(dictt)# this function is appent ont dictonary to another dictonary.
# # you only pass the update function to another dictornary..
# dic.update({"hello":333})
# print(dic)

#adding the new value...
dic["hello"]=330
print(dic)

#update the values
dic['aadarsh']=44
print(dic)

# print(dic.clear())// clear the dictonary
# print(dic)
dic.setdefault("helo",4) # set the defult value in dictonary..
print(dic)
