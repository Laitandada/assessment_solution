# 2.Alternate Min-Max Rearrangement

# Modify a given array of integers so that the first element is the smallest, the second is the largest, the third is the second-smallest, the fourth is the second-largest, and so on.

# Constraints:
# The input variable arr is a list of integers.
# The length of arr can be any non-negative integer.
# The elements in arr can be positive, negative, or zero.
# There are no specific constraints on the range of values for the elements in arr.



# -----------------------------Alternate MinMax Solution Explanation ---------------------------------------
#  Rearrange the array such that the first element is the smallest, the second is the largest,the third is the second-smallest, the fourth is the second-largest, and so on.

#  The solution sorts the array and then alternates between the smallest and largest remaining elements, appending them to the result list. It uses two pointers, one starting from the beginning of the sorted array and the other from the end, to achieve this.

#  The time complexity of this solution is O(n log n) due to the sorting step, and the space complexity is O(n) for the result list.
# Time Complexity: O(n log n)
# Space Complexity: O(n)


# -----------------------------Alternate MinMax Solution Code ---------------------------------------





def alternateMinMax(arr):
    # Sort the array in ascending order
    arr.sort()
    #  Initialize an empty list to store the rearranged elements.
    result = []
    # Initialize two pointers, left starting from the beginning and right starting from the end of the sorted array.
    left, right = 0, len(arr) - 1

    #  Iterate until the left pointer is less than or equal to the right pointer.
    while left <= right:
        # Append the smallest remaining element to the result list.
        result.append(arr[left])
        # Move the left pointer to the right.
        left += 1
        # If there are still elements remaining, append the largest remaining element to the result list.
        if left <= right:
            # Append the largest remaining element to the result list.
            result.append(arr[right])
            # Move the right pointer to the left.
            right -= 1

    # Return the rearranged list.
    return result

# ---------------------------------------Test cases-----------------------------------

print(alternateMinMax([13, 7, 8, 3, 2, 10, 15, -1]))
print(alternateMinMax([-5, -12, -1, 7, 14, -7, 3, 6]))
print(alternateMinMax([3, 6, 9, -10, -5, -2, 0, 8]))
print(alternateMinMax([]))                   
print(alternateMinMax([1]))                           
print(alternateMinMax([1, 1, 1, 1]))   