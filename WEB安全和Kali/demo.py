def twoSum(List, target):
    for i in range(len(List)):
        for j in range(len(List)):
            print(i, j)
            if i == j:
                continue
            else:
                if List[i] + List[j] == target:
                    return [i, j]


nums = [2, 7, 11, 33]
target = 9
nums.append()
print(twoSum(nums, target))
