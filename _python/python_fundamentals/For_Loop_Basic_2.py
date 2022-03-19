#1
def biggie_size(num_list):
    for i in range(len(num_list)):
        if num_list[i]>0:
            num_list[i]='big'
    return num_list
print(biggie_size([0,-5,-6,8,9,10]))

#2
def count_positives(array):
    count = 0
    for val in array:
        if val > 0:
            count += 1
    array[len(array)-1] = count
    return array
print([-5,-9,0,32,-6,22])
print(count_positives([-5,-9,0,32,-6,22]))


#3
def sum_total(array):
    sum = 0
    for val in array:
        sum += val
    return sum
print(sum_total([1,1,1,1]))
print(sum_total([1,1,1,55]))


# 4 
def avg(num_list):
    sum = 0
    for val in num_list:
        sum += val
    return (sum/len(num_list))
print(avg([5,5,5,6]))

# 5 
def lengthFun(num_list):
    return len(num_list)
print(lengthFun([1,1,1,1,1,4]))
print(lengthFun([1,1]))

# 6 
def minFun(num_list):
    min = num_list[0]
    for val in num_list:
        if val<min:
            min = val
    return min
print(minFun([600,80,99,26,3,5]))

# 8 
def ultimate_analysis(array):
    myDictonary = {'sumTotal': 0, 'average': 0, 'minimum': array[0], 'maximun': array[0], 'length': len(array)}
    for val in array:
        if myDictonary['minimum']<val:
            myDictonary['minimum'] = val
        if myDictonary['maximun']>val:
            myDictonary['maximun'] = val
        myDictonary['sumTotal']+= val
        myDictonary['average']=myDictonary['sumTotal']/len(array)
    return myDictonary
print(ultimate_analysis([1,2,1,2,4,0]))
print(ultimate_analysis([1,0]))
print(ultimate_analysis([15,4,1,0]))


# 9 
def reverse_list(array):
    for i in range(0, (len(array)-1)//2):
        temp = array[i]
        array[i] = array[len(array)-1-i]
        array[len(array)-1-i] = temp
    return array
print(reverse_list([11,12,13]))
print(reverse_list([11,12,13,14,15,16]))
print(reverse_list([11,12,13,14,15,16,18]))