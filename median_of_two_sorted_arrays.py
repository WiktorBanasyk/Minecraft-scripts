"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""
#example1
def findMedianSortedArrays():
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1 = [1,2]
        nums2 = [3,4]
        """
        nums1.extend(nums2)
        nums1.sort()
        """
        nums1 = sorted(nums1 + nums2)

        length = len(nums1)
        mid_index = length // 2

        if length % 2 == 1:
           return float(nums1[mid_index])
        else:
            return (nums1[mid_index] + nums1[mid_index - 1]) / 2.0

        #mid_index = length // 2

#print(nums1[mid_index])

result = findMedianSortedArrays()
print(result)
