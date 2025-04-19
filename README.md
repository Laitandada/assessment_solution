
## Read me for Plus One Assessment and Alternate Min Max Assessment 


## Overview
This repository contains solutions for the following assessments:
1. **Plus One Assessment**
2. **Alternate Min Max Assessment**

---

## Assessments

### 1. Plus One Assessment
The **Plus One Assessment** focuses on implementing a function that takes an array of digits representing a non-negative integer and increments the integer by one. The solution ensures proper handling of edge cases, such as carrying over when digits are `9`.

#### Example:
Input: `[1, 2, 3]`  
Output: `[1, 2, 4]`

Input: `[9, 9, 9]`  
Output: `[1, 0, 0, 0]`

#### Key Features:
- Handles arrays of varying lengths.
- Edge case handling for arrays with all `9`s.

---

### 2. Alternate Min Max Assessment
The **Alternate Min Max Assessment** involves rearranging an array such that elements alternate between the smallest and largest remaining values. This creates a zigzag pattern in the array.

#### Example:
Input: `[1, 2, 3, 4, 5]`  
Output: `[5, 1, 4, 2, 3]`

Input: `[-5, -12, -1, 7, 14, -7, 3, 6]`  
Output: `[-12, 14, -7, 7, -5, 6, -1, 3]`

#### Key Features:
- Sorts the array and alternates between min and max values.
- Works for arrays of both even and odd lengths.
- Works for arrays that contains negative values.


---

## How to Run
1. Clone the repository:
   git clone <repository-url>
   cd Miva-Assessment

2. Install Python

3. For Plus One Assessment 
   run python plus_one.py in your terminal

4. For Alternate Min Max Assessment 
   run python alternate_min_max.py your terminal