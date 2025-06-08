'''
DESCRIPTION
Given a sorted array of integers nums, determine if there exists a pair of numbers that sum to a given target.
Example:
Input: nums = [1,3,4,6,8,10,13], target = 13
Output: True (3 + 10 = 13)
Input: nums = [1,3,4,6,8,10,13], target = 6
Output: False
'''
def two_sum(arr, target):
    #print(f'received {arr}')
    i = 0
    j = len(arr)-1
    while i < j:
        target_ij = arr[i] + arr[j]
        if target_ij == target:
            print(arr[i], arr[j])
            return True
        elif target_ij > target:
            j -= 1
        else:
            i += 1
    return False

if __name__ == '__main__':
    print(two_sum([1,3,4,6,8,10,13], 13))
    print(two_sum([1,3,4,6,8,10,13], 6))
    print(two_sum([2,3,4], 6))