# Technical Test Solution

# 1. Plus One

# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

# Constraints:
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# digits does not contain any leading 0's.


# Plus One Solution

def plusOne(digits):
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

# Test cases

print(plusOne([1, 2, 3]))      
print(plusOne([4, 3, 2, 1])) 
print(plusOne([9]))      
print(plusOne([1, 2, 7]))     
print(plusOne([1, 9, 9]))    


# 2.Alternate Min-Max Rearrangement

# Modify a given array of integers so that the first element is the smallest, the second is the largest, the third is the second-smallest, the fourth is the second-largest, and so on.

# Constraints:
# The input variable arr is a list of integers.
# The length of arr can be any non-negative integer.
# The elements in arr can be positive, negative, or zero.
# There are no specific constraints on the range of values for the elements in arr.


def alternateMinMax(arr):
    arr.sort()
    result = []
    left, right = 0, len(arr) - 1

    while left <= right:
        result.append(arr[left])
        left += 1
        if left <= right:
            result.append(arr[right])
            right -= 1

    return result

# Test cases

print(alternateMinMax([13, 7, 8, 3, 2, 10, 15, -1]))
print(alternateMinMax([-5, -12, -1, 7, 14, -7, 3, 6]))
print(alternateMinMax([3, 6, 9, -10, -5, -2, 0, 8]))

