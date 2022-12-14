# Linked list

# Node class
"""With the basic implementation of setting the next node, getting the next node"""

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_node):
        self.next_node = new_node
    
    def __repr__(self):
        return str(self.value)

# Linked list class
class Linked_list:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node
    
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
    
    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()

        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
                current_node = current_node.get_next_node()
            
        return string_list
    
    def remove_node(self, value):
        current_node = self.get_head_node()

        if current_node.get_value() == value:
            self.head_node = current_node.get_next_node()

        else:
            while current_node:
                next_node = current_node.get_next_node()

                if next_node.get_value() == value:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node   

# ll = Linked_list(20)
# ll.insert_beginning(11)
# ll.insert_beginning(21)
# ll.insert_beginning(15)

# ll.remove_node(15)


# print(ll.get_head_node())
# print(ll.stringify_list())

"""QUEUES"""

class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0
    
    def enqueue(self, new_value):
        if self.has_space():
            item_to_add = Node(new_value)
            print("Adding " + str(item_to_add.get_value()))

            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print("Sorry no more room, we don't want a queue overflow!!")
    
    def dequeue(self):
        if not self.is_empty():
            item_to_remove = self.head
            print("Removing " + str(item_to_remove.get_value()))

            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("Queue is empty and we don't want a queue underflow")


    def get_size(self):
        return self.size
    
    def has_space(self):
        if self.max_size == None:
            return True
        else:
            return self.max_size > self.get_size()
    
    def is_empty(self):
        if self.get_size() == 0:
            return True
        else:
            return False 

    def peek(self):
        if self.is_empty():
            print("There is nothing to see here")
        else:
            return self.head.get_value()


# q = Queue(10)

# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# q.enqueue(40)
# q.enqueue(50)

# print(q.has_space())
# q.dequeue()
# print(q.peek())

"""STACKS"""

class Stack:
    def __init__(self, max_size=None):
        self.max_size = max_size
        self.top_item = None
        self.size = 0
    
    def push(self, new_value):
        if self.has_space():
            value_to_add = Node(new_value)
            print("Adding: " + str(value_to_add.get_value()))

            if self.is_empty():
                self.top_item = value_to_add
            else:
                value_to_add.set_next_node(self.top_item)
                self.top_item = value_to_add
            self.size += 1
        else:
            print("There is no space to add {} into the stack, we don't want a stack overflow!".format(new_value))
    
    def pop(self):
        if self.size > 0:
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()

            self.size -= 1

            return item_to_remove.get_value()
        else:
            print("Stack is empty, we dont want a stack underflow!!")

    def peek(self):
        if self.size > 0:
            return self.top_item.get_value()
        else:
            print("Nothing to see here!, have you tried the push function?")

    def get_size(self):
        return self.size
    
    def is_empty(self):
        if self.get_size() == 0:
            return True
        else:
            return False
    
    def has_space(self):
        return self.max_size > self.get_size()

# s = Stack(4)
# s.push(20)
# s.push(25)
# s.push(26)
# s.push(30)

# print(s.peek())

# s.pop()

# print(s.peek())

# s.push(50)
# s.push(400)


"""Search Algos"""

"""Linear Search"""
# number_list = [1, 2, 3, 4, 5, 10]

def linear(search_list, target_value):
    for value in range(len(search_list)):
        if search_list[value] == target_value:
            return value
    
    return "Not found"

# complexity of O(N)
# print(linear(number_list, 11))


"""Binary Search"""
def binary_search(search_list, target_value):

    mid_point = len(search_list) // 2
    midpoint_value = search_list[mid_point]

    if midpoint_value == target_value:
        return mid_point 
    
    if midpoint_value > target_value:
        left_half = search_list[:mid_point]
        return binary_search(left_half, target_value)

    if midpoint_value < target_value:
        right_half = search_list[mid_point + 1:]
        result = binary_search(right_half, target_value)

        return result + mid_point + 1

# number_list = [1, 2, 3, 4, 5, 10]
# print(binary_search(number_list, 5))

"""Sorting Algos"""

"""merge_sort"""
def merge_sort(list):
    if len(list) <= 1:
        return list

    mid_idx = len(list) // 2

    left_half = list[:mid_idx] 
    right_half = list[mid_idx:] 

    l = merge_sort(left_half)
    r = merge_sort(right_half)


    return merge(l, r)

def merge(l, r):
    sorted_array = []

    x = 0
    y = 0

    while x < len(l) and y < len(r):
        if l[x] <= r[y]:
            sorted_array.append(l[x])
            x += 1
        
        else:
            sorted_array.append(r[y])
            y += 1
    
    while x < len(l):
        sorted_array.append(l[x])
        x += 1 
    
    while y < len(r):
        sorted_array.append(r[y])
        y += 1

    return sorted_array


# number_list = [5, 3, 1]
# print(merge_sort(number_list))


"""Quick sort"""
"""n log n"""
"""Worst case O(n^2)"""
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = []
    right = []

    for value in range(1, len(arr)):
        if arr[value] < pivot:
            left.append(arr[value])
        else:
            right.append(arr[value])
    
    left_side = quick_sort(left)
    right_side = quick_sort(right)

    return left_side + [pivot] + right_side

# number_list = [5, 3, 1, 2, 4]
# print(quick_sort(number_list))

"""Selection sort"""
"""worst case, O(N^2)"""
def selection_sort(arr):
    for value in range(len(arr)):
        min_value = value

        for element in range(value + 1, len(arr)):
            if arr[element] < arr[min_value]:
                min_value = element
        
        if min_value != value:
            arr[value], arr[min_value] = arr[min_value], arr[value]
    
    return arr

# number_list = [5, 3, 1, 2, 4]
# print(selection_sort(number_list))

"""Bubble sort"""
"""Worst case O(N^2)"""

def bubble_sort(arr):
    # Set a flag to track whether any swaps have been made
    swapped = True

    # Keep looping until no swaps are made
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            # If the current element is greater than the next element, swap them
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
    return arr

# number_list = [5, 3, 1, 2, 4]
# print(bubble(number_list))

"""
OPtimised Merge sort

"""
def merge_sort(arr):

    isSorted = False
    i = 1

    if len(arr) <= 1:
        return arr
    
    while i < len(arr):
        if(arr[i] < arr[i - 1]):
            isSorted = True
        i += 1
        
    if (not isSorted) :
        return arr
    else :

        mid = len(arr) // 2

        left_side = arr[:mid]
        right_side = arr[mid:]

        # print(len(arr))

        l = merge_sort(left_side)
        r = merge_sort(right_side)
        # print(l)
        # print(r)

        return merge(l, r)

"""Function that does the merging of the arrays"""

def merge(a, b):

    sorted_array = []

    x = 0 
    y = 0 

    len_a = len(a) 
    len_b = len(b) 

    while x < len_a and y < len_b:

        if a[x] <= b[y]:
            sorted_array.append(a[x])
            x += 1
            
        else:
            sorted_array.append(b[y])
            y += 1  
                  
        
    while x < len_a:
        sorted_array.append(a[x])
        x += 1
        

    while y < len_b:
        sorted_array.append(b[y])
        y += 1
        

        # print(sorted_array)

    return sorted_array





















