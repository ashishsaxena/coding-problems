'''
Given an integer input array heights representing the heights of vertical lines, write a function that returns the maximum area of water that can be contained by two of the lines (and the x-axis). The function should take in an array of integers and return an integer.

Example 1:
Inputs: heights = [3,4,1,2,2,4,1,3,2]
Output: 21

Example 2:
Inputs: heights = [1,2,1]
Output: 2
'''


def max_container(arr):
    i = 0
    j = len(arr) - 1
    max_vol = -1
    while i<j:
        width = j-i
        if arr[i] > arr[j]:
            vol = width * arr [j]
            max_vol = max_vol if max_vol > vol else vol
            j -= 1
        else:
            vol = width * arr [i]
            max_vol = max_vol if max_vol > vol else vol
            i += 1
    print(f'{arr} -> {max_vol}')
    return max_vol



if __name__ == '__main__':
    max_container([3,4,1,2,2,4,1,3,2])
    max_container([1,2,1])
    max_container([1,8,6,2,5,4,8,3,7])