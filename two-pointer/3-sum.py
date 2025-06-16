def three_sum(nums: list[int], target):
    if len(nums) < 3:
        return []
    nums = sorted(nums)
    result = []
    for i in range (0, len(nums)-2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while(left < right):
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            else:
                if current_sum > target:
                    right -= 1
                elif current_sum < target:
                    left += 1
    return result

if '__main__' in __name__:
    print(three_sum([-1,0,1,2,-1,-1], -3) == [[-1, -1, -1]])
    print(three_sum([-1,0,1,2,-1,-1], -2) == [[-1, -1, 0]])
    print(three_sum([-1,0,1,2,-1,-1], -1) == [[-1, -1, 1]])
    print(three_sum([-1,0,1,2,-1,-1], 0) == [[-1, -1, 2], [-1, 0, 1]])
    print(three_sum([-1,0,1,2,-1,-1], 1) == [[-1, 0, 2]])
    print(three_sum([-1,0,1,2,-1,-1], 2) == [[-1, 1, 2]])
    print(three_sum([-1,0,1,2,-1,-1], 3) == [[0, 1, 2]])
    print(three_sum([-1,0,1,2,-1,-4], 0) == [[-1,-1,2],[-1,0,1]])
    print(three_sum([0,0,0], 0) == [[0,0,0]])
    print(three_sum([1,2,-2,-1], 0) == [])
    print(three_sum([-4,-2,-2,-2,0,1,2,2,2,2,2,3], 0) == [[-4,1,3],[-4,2,2],[-2,0,2]])
    