def containsDuplicate(nums):
    sorted_nums = sorted(nums)

    for i in range(len(nums) - 1):

        if sorted_nums[i] == sorted_nums[i + 1]:
            return True
    return False
