from random import randint
import sys
import re

def object_merge(list1, list2):
    return list1 + list2

def object_inner_merge(outer_list, inner_list):
    # min_index = 0
    # max_index = len(outer_list.items)
    # while outer_list.items[min_index] < inner_list.min: #could use binary search to achieve this process
    #     min_index += 1
    # while outer_list.items[max_index] > inner_list.max: #could use binary search to achieve this process
    #     max_index -= 1
    min_index = binary_search(outer_list, inner_list[0])
    max_index = binary_search(outer_list, inner_list[-1])
    return outer_list[0:min_index] + merge_sorted_lists(outer_list[min_index: max_index], inner_list) + outer_list[max_index:]
    
def object_overlap_merge(left_list, right_list):
    right_list_min_index = binary_search(left_list, right_list[0])
    left_list_min_index = binary_search(right_list, left_list[-1])
    left_overlap = left_list[right_list_min_index:]
    right_overlap = right_list[:left_list_min_index]
    overlap = merge_sorted_lists(left_overlap, right_overlap)  
    return left_list[:right_list_min_index] + overlap + right_list[left_list_min_index:]
   
def merge_sorted_lists(list1, list2):
    reversed_list1 = list1
    reversed_list2 = list2
    reversed_list1.reverse()
    reversed_list2.reverse()
    #print(reversed_list1, reversed_list2)
    new_list = list()
    for i in range(len(list1)+ len(list2)):
       # print(new_list)
        
        if len(reversed_list1) != 0 and len(reversed_list2) != 0:
            if reversed_list1[-1] > reversed_list2[-1]:
                new_list.append(reversed_list2.pop())
            else:
                new_list.append(reversed_list1.pop())
        elif len(reversed_list1) == 0:
            new_list.append(reversed_list2.pop())
        else:
            new_list.append(reversed_list1.pop())
    return new_list
def binary_search(lis: list(), target) -> int(): #finds the location where the following item SHOULD be, not is
    search_range_max = len(lis)
    search_range_min = 0
    mid_i = 0 
    while lis[mid_i] != target and len(lis[search_range_min: search_range_max]) > 1:
        print("range", search_range_min, search_range_max)
        print("size of range", search_range_max - search_range_min)
       # print("mid_i: %s lis at mid_i: %s, lis at min %s, lis at max %s" % (str(mid_i), str(lis[mid_i]), str(lis[search_range_min]), str(lis[search_range_max])))
        mid_i = search_range_min + ((search_range_max - search_range_min) // 2 )
        if lis[mid_i] < target:
            search_range_min = mid_i
        else:
            search_range_max = mid_i

        if len(lis[search_range_min: search_range_max]) == 1:
            if mid_i == 1 and lis[0] > target:
                mid_i = 0
        print("range", search_range_min, search_range_max)
        
        print("mid_i", mid_i)
        
    print(mid_i)
    return mid_i

def generate_random_sorted_list() -> list():
    x = 0
    lis = list()
    while x < 10 and len(lis) < randint(5,10):
        x = randint(x,10)
        lis.append(x)

    return lis

def merge(lis):
    
    print("big list", lis)

    if len(lis) > 1:
        #print(lis)
        mid = len(lis)//2
        lis1 = lis[:mid]
        lis2 = lis[mid:]
        
       
        
        new_lis = list()
        new_lis1 = merge(lis1)
        new_lis2 = merge(lis2)
        new_lis1_min = new_lis1[0]
        new_lis1_max = new_lis1[-1]
        new_lis2_min = new_lis2[0]
        new_lis2_max = new_lis2[-1]
        print("lis1 %s \n lis2 %s" % (new_lis1, new_lis2))
        print("lis1min %s lis1max %s lis2min %s lis2max %s" % (new_lis1_min, new_lis1_max, new_lis2_min, new_lis2_max))
        if new_lis1_min >= new_lis2_max:
            print(1)
            new_lis = object_merge(new_lis2, new_lis1)
        elif new_lis1_max <= new_lis2_min:
            print(2)
            new_lis = object_merge(new_lis1, new_lis2)
        elif new_lis1_min >= new_lis2_min and new_lis1_max <= new_lis2_max:
            print(3)
            new_lis = object_inner_merge(new_lis2, new_lis1)
        elif new_lis2_min >= new_lis1_min and new_lis2_max <= new_lis1_max:
            print(4)
            new_lis = object_inner_merge(new_lis1, new_lis2)
        elif new_lis1_min < new_lis2_min and new_lis1_max > new_lis2_min: # all cases where lis1.max > lis2.max should be taken into account by previous clause, but keep aware
            print(5)
            new_lis = object_overlap_merge(new_lis1, new_lis2)
        else: 
            print(6)
            new_lis = object_overlap_merge(new_lis2, new_lis1)
        print("return list", new_lis)
        return new_lis
    else:
        print("return list", lis)
        return lis

def main():
     
    try:
        lis = list(sys.argv[1])
        lis = [x for x in lis[1:-2] if x.isdigit()]
        print(lis)
        print("hello")
    except:
        lis = list()
        for i in range(randint(50,100)):
            lis.append(randint(0, 9))
    
    # lis = [6, 5, 0]
    # print(lis)
    sorted_lis = merge(lis)

    print(sorted_lis)
    #list1 =  [1, 8, 9, 10]
    # list1 = generate_random_sorted_list() 
    # #list2 = generate_random_sorted_list()
    # print(list1)
    # print(binary_search(list1, 5))
    
    #print(binary_search(list2, 5))
    #print(merge_sorted_lists(list1, list2))

if __name__ == "__main__":
	main()
