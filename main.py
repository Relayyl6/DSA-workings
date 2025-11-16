# def take_magic_damage(health, resist, amp, spell_power):
#     max_damage = spell_power * amp

#     actual_damage = max_damage - resist

#     new_health = health - actual_damage
#     return new_health   


# merge_sort sorting algorithm
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])

#     return merge(left, right)

# def merge(left, right):
#     result = []
#     while left and right:
#         if left[0] <= right[0]:
#             result.append(left.pop(0))
#         else:
#             result.append(right.pop(0))
#     result.extend(left)
#     result.extend(right)
#     return result

# # Example
# arr = [54, 32, 62, 87, 21, 56, 9, 43]
# sorted_arr = merge_sort(arr)
# print("Sorted array:", sorted_arr)



# # bubble sort algorithm 
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n): # for each between 0, 1, 2, 3, 4, 5, 6, 7 ... (length of array( which is n) -1)
#         for j in range(0, n - i - 1): # compares thm with adjacent elemtnts 
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr

# # Example
# arr = [54, 32, 62, 87, 21, 56, 9, 43]
# sorted_arr = bubble_sort(arr)
# print("Sorted array:", sorted_arr)



# free code camp daily challenge solved. Iterative procedure to coming about answer will be uploaded to a readme later

# Question
# Given an array and an integer representing how many positions to shift the array, return teh shifted array.
# A positive integer shifted teh array to the left while a negative integer shifted the array to the right
# The shift wrap around the array. eg [1, 2, 3] and 1, shifts the array to the left returning [2, 3, 1]
# def sort_array(arr, k):
#     n = len(arr)
#     if k < 0: # if k is a negative value
#         L = n - (abs(k) % n)
#     else: # if k is a positive shift or shift(k) is greater than the length of the array
#         L = k % n

#     new_array = arr[L:] + arr[:L]
#     return new_array

# # Example
# arr = [54, 32, 62, 87, 21, 56, 9, 43]
# shifted_arr = sort_array(arr, 4)
# print("Sorted array:", shifted_arr)