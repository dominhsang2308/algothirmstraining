# def selection_sort(n):
#     for i in range(len(n)):
#         for j in range(i + 1, len(n)):
#             if n[i] > n[j]:
#                 n[i],n[j] = n[j],n[i]
#     return n


# def buble_sort(n):
#     for _ in range(len(n)):
#         for i in range(len(n) - 1):
#             if n[i] > n[i+1]:
#                 n[i], n[i+1] = n[i+1], n[i]
#     print(i + 1, '-' ,n)


# minArr = [3,2,6,8,9]
# min = minArr[0]
# for i in minArr:
#     if i < min:
#         min = i
    
# print(f'Min : {min}')

# arr = [3,6,1,9,8,10]
# max = 0
# for i in arr:
    
#     if i > max:
#         max = i
# print(f'Max : {max}')

# def tim_nhi_phan(mang,x):
#     trai = 0
#     phai = len(mang) -1 
#     while trai <= phai:
#         giua = (trai + phai) // 2

#         if mang[giua] == x:
#             return giua
#         if x < mang[giua]:
#             trai = giua - 1
#         else:
#             phai = giua + 1
#     return -1

# def tim_tuyen_tinh(mang,x):
#     for i in range(len(mang)):
#         if mang[i] == x:
#             return i
#     return -1

# def twoSum(n,target):
#     for i in range(len(n)):
#         for j in range(i+1,(len(n))):
#             if n[i] + n[j] == target:
#                 return [i,j]
#             else:
#                 return False

# print(twoSum([2,7,8,11],9))

def insert_sort(mang):
    for i in range(len(mang)):
        temp = mang[i]
        j = i
        while j > 0 and mang[j - 1] > temp:
            mang[j] = mang[j- 1]
            j = j -1
        mang[j] = temp
    return mang
print(insert_sort([5,4,3,2,1]))
