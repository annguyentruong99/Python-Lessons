# Given an list of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

# # starting function, (hint: use dictionary)
# def twoSum(nums: list[int], target: int) -> list[int]:
#   pair = {}
#   index = 0
#   for num in nums:
#     if num in pair:
#       return [pair[num], index]
#     else:
#       pair[target - num] = index
#       index = index + 1

# twoSum([2,7,11,15], 9)

# pair = {} 
# i = 0
# for num in nums: # 2, 7, 11, 15

# pair = {7: 0}
# pair[7]

# twoSum([2,3,4], 6)

# pair = {}
# i = 0
# for num in nums: #2, 3, 4
# #2
# pair = {
#   4: 0
# }
# index = 1

# #3
# pair = {
#   4: 0,
#   3: 1
# }
# index = 2
# #4

# inputs:
#   tuition = 8000
#   increase_rate = 0.03

# Calculation:
#   increase_amount = 8000 * 1.03 

# output:
#   increase_amount

def main():
  tuition = int(input("Enter your tuition: "))
  increase_rate = int(input("Enter your rate in percentage: "))
  for i in range(5):
    tuition = tuition * (1 + increase_rate/100)
    print("$" + tuition)

main()