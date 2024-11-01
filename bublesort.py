#Sắp xếp theo thứ tự tăng dần

# arrUp = [3,5,4,8,6,9,7]
# temp = 0
# for _ in range(len(arrUp) - 1):
#     for i in range(len(arrUp) - 1):
#         if arrUp[i] > arrUp[i+1]:
#             temp = arrUp[i]
#             arrUp[i] = arrUp[i+1]
#             arrUp[i+1] = temp
# print(arrUp)

#Sắp xếp theo thứ tự giảm dần
# arrDown = [3,5,4,8,6,9,7]

# Downtemp = 0

# for _ in range(len(arrDown) -1):
#     for i in range(len(arrDown) -1):
#         if arrDown[i] < arrDown[i+1]:
#             Downtemp = arrDown[i]
#             arrDown[i] = arrDown[i+1]
#             arrDown[i+1] = Downtemp
# print(arrDown)


#Đếm có bao nhiêu số 9 xuất hiện trong mảng

# countArr = [4,4,6,3,9,9,9,2,9]

# count = 0
# newArry = []
# for i in countArr:
#     if i %2 ==0:
#         count = count + 1
#     else:
#         newArry.append(i)
# print(count , newArry)

# def twoSum(n,target):
#     for i in range(len(n)):
#         for j in range(i+1,(len(n))):
#             if n[i] + n[j] == target:
#                 return [i,j]
#             else:
#                 return False

# print(twoSum([2,7,8,11],9))

arrUp = [1,3,5,4,6]
def bubleSort(nums):
    for _ in range(len(nums) -1):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                nums[i],nums[i+1] = nums[i+1],nums[i]
    return nums
print(bubleSort(arrUp))