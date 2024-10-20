# YOUR CODE HERE

list1 = []
list2 = []

n = int(input())

for i in range(n):
    yo = int(input())
    list1.append(yo)

for i in range(n):
    yo = int(input())
    list2.append(yo)

def summation(list1,list2):
    updated_list = []
    global n
    for i in range(n):
        sum = list1[i]+list2[i]
        updated_list.append(sum)
    return updated_list
updated_list = summation(list1,list2)

print(summation(list1,list2))

def find_min_max(updated_list):
    min = updated_list[0]
    max = updated_list[0]
    for i in updated_list :
        if i < min:
            min = i

    for i in updated_list :
        if i > max:
            max = i

    find_min_max = (min,max)
    return find_min_max

print(find_min_max(updated_list))
