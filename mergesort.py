from random import randint
class Merge_List:
    def __init__(self, items = None, lismax, lismin):
        self.items = items
        self.max = self.items[len(self.items)]
        self.min = self.items[0]

    def object_merge(self, list1, list2):
        self.items = list1.items + list2.items
        self.max = list2.max
        self.min = list1.min

   
    def object_inner_merge(self, outer_list, inner_list):
        # min_index = 0
        # max_index = len(outer_list.items)
        # while outer_list.items[min_index] < inner_list.min: #could use binary search to achieve this process
        #     min_index += 1
        # while outer_list.items[max_index] > inner_list.max: #could use binary search to achieve this process
        #     max_index -= 1
        min_index = binary_search(outer_list.items, inner_list.min)
        max_index = binary_search(outer_list.items, inner_list.max )
        self.items = outer_list.items[0:min_index] + merge_sorted_lists(outer_list.items[min_index: max_index], inner_list.items) + outer_list.items[max_index:]
        self.max = outer_list.max
        self.min = outer_list.min
    def object_overlap_merge(self, left_list, right_list):
        right_list_min_index = binary_search(left_list.items, right_list.min)
        left_list_min_index = binary_search(right_list.items, left_list.max)
        left_overlap = left_list[right_list_min_index:]
        right_overlap = right_list[:left_list_min_index]
        overlap = merge_sorted_lists(left_overlap, right_overlap)  
        self.items = left_list[:right_list_min_index] + overlap + right_list[left_list_min_index:]
        self.max = right_list.max
        self.min = left_list.min
def merge_sorted_lists(list1, list2):
    reversed_list1 = list1
    reversed_list2 = list2
    reversed_list1.reverse()
    reversed_list2.reverse()
    print(reversed_list1, reversed_list2)
    new_list = list()
    for i in range(len(list1)+ len(list2)):
        print(new_list)
        
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
    
    if type(lis) == list:
        length_list = len(lis)
    else:
        length_list = len(lis.items)
        lis = lis.items
    
    if length_list > 1:
        print(lis)
        mid = len(lis)//2
        lis1 = Merge_List(lis[:mid])
        lis2 = Merge_List(lis[mid:])
       
        new_lis = Merge_List()
        
        
        if lis1.min > lis2.max:
            new_lis.object_merge(merge(lis1), merge(lis2))
        elif lis2.min > lis1.max:
            new_lis.object_merge(merge(lis2), merge(lis1))
        elif lis1.min > lis2.min and lis1.max < lis2.max:
           new_lis.object_inner_merge(merge(lis2), merge(lis1))
        elif lis2.min > lis1.min and lis2.max < lis1.max:
            new_lis.object_inner_merge(merge(lis1), merge(lis2))
        elif lis1.min < lis2.min and lis1.max > lis2.min: # all cases where lis1.max > lis2.max should be taken into account by previous clause, but keep aware
            new_lis.object_overlap_merge(merge(lis1), merge(lis2))
        else: 
            new_lis.object_overlap_merge(merge(lis2), merge(lis1))
        return new_lis
    else:
        return Merge_List(lis)

def main():
	lis = list()
	for i in range(randint(0,5)):
		lis.append(randint(0, 5))

	print(lis)

	sorted_lis = merge(lis)

	print(sorted_lis.items)
    #list1 =  [1, 8, 9, 10]
    # list1 = generate_random_sorted_list() 
    # #list2 = generate_random_sorted_list()
    # print(list1)
    # print(binary_search(list1, 5))
    
    #print(binary_search(list2, 5))
    #print(merge_sorted_lists(list1, list2))

if __name__ == "__main__":
	main()
