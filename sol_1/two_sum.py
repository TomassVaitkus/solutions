class Solution:
    def twoSum(self, nums, target):
        nums_with_indices = [(num, idx) for idx, num in enumerate(nums)]
        nums_with_indices.sort(key=lambda x: x[0])
        
        left, right = 0, len(nums_with_indices) - 1
        
        while left < right:
            current_sum = nums_with_indices[left][0] + nums_with_indices[right][0]
            if current_sum == target:
                return [nums_with_indices[left][1], nums_with_indices[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []

# Skuriame Solution objektą
solution = Solution()

# Sukuriame norimą sąrašą skaičių
numbers = [4, 2, 7, 1, 5, 9]

# Surandame porą, kurios suma lygi target_sum:
target_sum = 11
result_indices = solution.twoSum(numbers, target_sum)

if result_indices:
    print(result_indices)
else:
    print("Could not find any pair")