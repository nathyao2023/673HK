#question 5
#Write a function that combines two lists by alternatingly
#taking elements, e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3] and
#test it in your program.



#

def combine_lists(list1, list2):
    combined_list = []
    for i in range(max(len(list1), len(list2))):
        if i < len(list1):
            combined_list.append(list1[i])
        if i < len(list2):
            combined_list.append(list2[i])
    return combined_list

#test 1
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
print(combine_lists(list1, list2))
#test 2
list11 = ['h','l','o']
list22 = ['e','l']
print(combine_lists(list11,list22))
