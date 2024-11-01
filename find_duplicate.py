
# def find_duplicate(nums):
#     nums.sort()
#     new_array = []
#     for i in range(len(nums) - 1):
#         if nums[i] == nums[i+1]:
#             nums.remove(nums[i])
#             new_array.append(nums[i])
#     return new_array

# print(find_duplicate([1,1,2]))

# def remove_duplicate(nums):
#     count = 0
#     new_array = []
#     for i in range(len(nums) - 1):
#         for j in range(i+1, len(nums)):
#             if nums[i] == nums[j]:
#                 count += 1
#     return count

# print(remove_duplicate([1,1,2]))

list1 = [1,2,4]
list2 = [1,3,4]
list3 = list1 + list2
list3.sort()
print(list3)