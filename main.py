# def take_magic_damage(health, resist, amp, spell_power):
#     max_damage = spell_power * amp

#     actual_damage = max_damage - resist

#     new_health = health - actual_damage
#     return new_health   


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result

# Example
arr = [54, 32, 62, 87, 21, 56, 9, 43]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
