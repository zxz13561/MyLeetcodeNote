
def two_sum(nums, target):
    dic = {}
    for i in range(len(nums)):
        if target - nums[i] in dic:
            return [dic[target - nums[i]], i]
        else:
            dic[nums[i]] = i


if __name__ == '__main__':
    print(two_sum([1, 3, 4, 9], 12))
