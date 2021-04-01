
def sum(fun,value): # fun variable contain a lambda function. always contain the lambda 
                        #funcion return value..
    data=str(fun)+" "+value
    print(data)
 


var= lambda x:x
# it is a one line function./
#         # you can pass the funcion in any another funcion.\
#         # if you pass the funcion in another funcion. funcion return value hass been replased 
            # in 
#           # formal argument.


sum(var("hello"),var("aadarsh"))  # passing the lembda funcion as a argument. in 
#                                     #another funcion. funcion
#                         # sum funcion first call a var lambda funcion, or when lembda funcion return the value. then sum function call the both the value..



#lambda function another example...

            #lambda funcion with filter.
l1=[334,6,7,6,5,54,45,7,45,7,56,4,5]
finil_list =list(filter(lambda x:(x%2==0),l1)) # filter always itrable argiment and funcions. 
                                                 # filter always itrable argiment and funcions. 

print(finil_list)





# lambda funcion map.\

f_list=list(map(lambda x:x*3,finil_list))  # every element of finil_list call the lambda  
                                            #  function.. and it return the value of map..
print(f_list)