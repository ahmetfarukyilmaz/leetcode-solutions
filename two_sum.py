def twoSum(nums, target):
    result = []

    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[j] + nums[i] == target and i != j:
                result.append(i)
                result.append(j)
                return result
