'''
Given an integer input array heights representing the heights of vertical lines, write a function that returns the maximum area of water that can be contained by two of the lines (and the x-axis). The function should take in an array of integers and return an integer.

Example 1:
Inputs: heights = [3,4,1,2,2,4,1,3,2]
Output: 21

Example 2:
Inputs: heights = [1,2,1]
Output: 2
'''


def max_container(heights):
    left, right = 0, len(heights) - 1
    max_area = 0
    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        current_area = width * height
        max_area = max(current_area, max_area)
        if heights[left] > heights[right]:
            right -= 1
        else:
            left += 1
    return max_area



if __name__ == '__main__':
    max_container([3,4,1,2,2,4,1,3,2])
    max_container([1,2,1])
    max_container([1,8,6,2,5,4,8,3,7])
