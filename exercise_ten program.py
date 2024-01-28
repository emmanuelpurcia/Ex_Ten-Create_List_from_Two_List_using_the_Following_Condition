# Hello! This program creates a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

# pseudocode

# Function to merge list from first list and second list
def merge_list(list1, list2):
    # Add odd numbers from list 1
    result_list = [num for num in list1 if num % 2 != 0]
    # Add even numbers from list 2
    result_list += [num for num in list2 if num % 2 == 0]  
    return result_list

# Given Lists
print("The Given Lists Are:")
list1 = [10, 20, 25, 30, 35]
print("list1 = [10, 20, 25, 30, 35]")
list2 = [40, 45, 60, 75, 90]
print("list2 = [40, 45, 60, 75, 90]")
# Print merge list
print("result list:", merge_list(list1, list2))
