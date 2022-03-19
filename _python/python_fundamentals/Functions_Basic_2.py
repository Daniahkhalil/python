#1
def countdown(num):
    coundownl=[]
    for i in range(num,-1,-1):
        coundownl.append(i)
    return coundownl
      

# print(countdown(12))

#2 
def printlist(num_list):
    print(num_list[0])
    return num_list[1]
# print(printlist([1,2]))

#3
def first_plus_length(num_list):
    first_val=num_list[0]
    length_of_list=len(num_list)
    return first_val+length_of_list
# print(first_plus_length([1,2,3,4]))

#4
def val_greater(num_list):
    new_list=[]
    sc_val=num_list[1]
    for i in range(len(num_list)):
        if num_list[i] > sc_val:
            new_list.append(num_list[i])
    print(len(num_list))
    return num_list
val_greater([1,2,3,5,7,5])

def length_val(size,value):
    new_list=[]
    for i in range(size):
        new_list.append(value)
    return new_list





