
def bubble_sort(list):
    exchanges = True
    numb = len(list)-1
    while numb > 0 and exchanges:
        exchanges = False
        for i in range(len(list)):
            if list[i-1]>list[i]:
                list[i-1], list[i] = list[i], list[i-1]
                exchanges = True
        numb -= 1
    return list
print(bubble_sort([3, 2, 4, 7, 6, 1]))
def selection_sort(list):
    newlist = []
    numb = len(list)-1
    while numb > 0:
        max = 0
        for i in range(len(list)):
            if list[i] > max:
                max = list[i]
                maxindex = i
        newlist.append(max)
        list.pop(maxindex)
        numb -= 1
    newlist.reverse()
    return newlist
print(selection_sort([9,1,34,7,2,3,45,6,78,56,36,65,33,21,23,34,45,6]))
