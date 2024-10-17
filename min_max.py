arr = [3,6,1,9,8]
max = 0
for i in arr:
  
    if i > max:
        max = i
print(f'Max : {max}')

#Find min 

minArr = [3,2,6,8,9]
min = minArr[0]
for i in minArr:
    if i < min:
        min = i
    
print(f'Min : {min}')

# tính trung bình cộng

dayso = [3,4,5,6,7,9]
tong = 0

for i in dayso:
    tong = tong + i
    trungbinhcong = tong/len(dayso)
print(trungbinhcong)

#trung bình cộng các số lẻ

daysole = [3,5,7,9]
tongsole = 0
print(len(daysole))
for i in daysole:
    tongsole = tongsole + i
    trungbinhcong = tongsole / len(daysole)
    chiachoba = trungbinhcong / 3
print(chiachoba)