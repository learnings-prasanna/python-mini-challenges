# --------------
def palindrome(num):
    temp=num
    while True:
        temp= int(temp)+1
        check=str(temp)
        if check[::-1]==check:
            return temp
            break
    
palindrome(13456)


# --------------
from collections import Counter
import numpy as np
def a_scramble(str_1,str_2):
    str_1 = list(str_1.replace(" ","").lower())
    str_1.sort()
    str_2 = list(str_2.replace(" ","").lower())
    str_2.sort()
    dict1 = Counter(str_1)
    dict2 = Counter(str_2)
    common = dict1 & dict2
    keys1 = dict1.keys()
    value1 = list(dict1.values())
    print(keys1,value1)
    keys2 = dict2.keys()
    value2 = list(dict2.values())
    print(keys2,value2)
    keys3 = common.keys()
    value3 = list(common.values())
    print(keys3,value3)
    if (keys3 == keys2 ):
        value3 = np.asarray(value3)
        value2 = np.asarray(value2)
        return not (value3 - value2).sum()
    else:
        return False
print(a_scramble("baby shower","shows"))
print(a_scramble("labratory","Bat"))
print(a_scramble("eatcher","teacher"))




# --------------
#Code starts here
def check_fib(num):
    n1 = 0
    n2 = 1
    if num==0 or num==1:
        return True

    while n2 < num:
       nth = n1 + n2
       if nth == num:
           return True
       # update values
       n1 = n2
       n2 = nth
    return False
print(check_fib(377))


# --------------
#Code starts here
import numpy as np
def compress(word):
    count = 1
    list2=[]
    list1 = list(word.lower())
    '''
    for idx,letter in enumerate(list1):
        if list1[idx] == list1[idx-1]:
            count+=1
            continue
        elif (idx==0 and list1[1]!=list1[0]): 
            print(letter,count)
            list2.append(letter)
            list2.append(str(count))
        elif (list1[idx] != list1[idx-1]):
            list2.append(list1[idx-1])
            list2.append(str(count))
            count=1
        '''
    for i in range(len(list1)):
        if (i+1 > len(list1)-1):
            list2.append(list1[i])
            list2.append(str(count))
            break
        elif list1[i+1]==list1[i]:
            count+=1
        else:
            list2.append(list1[i])
            list2.append(str(count))
            count=1
        
    list2 = "".join(list2)
    return list2
print(compress("sggtts"))



# --------------
#Code starts here
def k_distinct(string,k):
    dict1 = {}
    list1 = list(string.lower())
    for letter in list1:
        if letter not in dict1:
            dict1[letter]=1
        else:
            dict1[letter]+=1
    keys = len(dict1.keys())
    return (keys==k)
print(k_distinct('banana',4))



