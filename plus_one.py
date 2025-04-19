# Technical Test Solution

# 1. Plus One

# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

# Constraints:
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# digits does not contain any leading 0's.


# -----------------------------Plus One Solution Explanation ---------------------------------------

# this solution to the plus one assessment rearranges the array such that the first element is the smallest, the second is the largest, the third is the second-smallest, the fourth is the second-largest, and so on.

# The solution iterates through the array from the last element to the first, checking if the current digit is less than 9. If it is, it increments that digit by 1 and returns the modified array. If the digit is 9, it sets it to 0 and continues to the next digit. If all digits are 9, it returns a new array with a leading 1 followed by zeros.

# The time complexity of this solution is O(n), where n is the length of the input array. This is because we iterate through the array once, and the space complexity is O(1) since we are modifying the input array in place and not using any additional data structures.

# Time Complexity: O(n)
# Space Complexity: O(1)


# -----------------------------Plus One Solution Code ---------------------------------------


def plusOne(digits):
    # constraints validation
    if not (1 <= len(digits) <= 100):
        raise ValueError("The length of the digits array must be between 1 and 100.")
    if not all(isinstance(d, int) and 0 <= d <= 9 for d in digits):
        raise ValueError("The digits in the array must be integers between 0 and 9.")
    for d in digits:
        if isinstance(d, int) and d != 0 and d < 10:
            continue
        raise ValueError("digits does not contain any leading 0's.")
    
    #  Determine the length of the array
    n = len(digits)
    # Iterate through the array from the last element to the first
    for i in range(n - 1, -1, -1):
        # If the current digit is less than 9, increment it and return the array
        if digits[i] < 9:
            # Increment the current digit by 1
            digits[i] += 1
            # Return the modified array
            return digits
        # If the current digit is 9, set it to 0 and continue to the next digit
        digits[i] = 0
        # If all digits are 9, we need to add a new digit at the beginning
        # Create a new array with a leading 1 followed by zeros
    return [1] + digits


# --------------------------------------Test cases----------------------------------------
# print(plusOne([0, 012, 2])) edge case for leading zero 
print(plusOne([1, 9, 9])) 
print(plusOne([])) 
print(plusOne([1, 2, 3, 100])) 
print(plusOne([1, 2, 7]))   
print(plusOne([1234])) 
print(plusOne([1, 2, 3]))      
print(plusOne([4, 3, 2, 10])) 

print(plusOne([4, 3, 2, 7])) 
print(plusOne([10, 10, 10, 10])) 
print(plusOne([9]))      
print(plusOne([9, 9, 9])) 
print(plusOne([0]))     




