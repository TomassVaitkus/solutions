class PairFinder:
    def __init__(self, nums):
        self.nums = nums
        self.nums.sort()
    
    def find_pair_with_sum(self, target):
        left, right = 0, len(self.nums) - 1
        
        while left < right:
            current_sum = self.nums[left] + self.nums[right]
            if current_sum == target:
                return (self.nums[left], self.nums[right])
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return None

# Creating a list of numbers
numbers = [4, 2, 7, 1, 5, 9]

# Sukurkite PairFinder objektą
pair_finder = PairFinder(numbers)

# Lets sefine target_sum and his elements indexes:
target_sum = 11
result = pair_finder.find_pair_with_sum(target_sum)

if result:
    print([numbers.index(result[0]), numbers.index(result[1])])
else:
    print("There's no pair")