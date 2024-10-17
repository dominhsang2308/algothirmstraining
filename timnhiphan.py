import random
def sang_sinh_mang_tang_dan(n):
    mang = []
    so_dau_tien = random.randint(-100,100)
    mang.append(so_dau_tien)

    for i in range(1,n):
        tang = random.randint(1,10)
        so = mang[i-1] + tang
        mang.append(so)
    return mang


def tim_nhi_phan(mang,x):
    trai = 0
    phai = len(mang) -1 
    while trai <= phai:
        giua = (trai + phai) // 2

        if mang[giua] == x:
            return giua
        if x < mang[giua]:
            trai = giua - 1
        else:
            phai = giua + 1
    return -1
        
def main():
    mang = sang_sinh_mang_tang_dan(10)
    print(mang)
    x = int(input('Nhập vào vị trí : '))
    vitri = tim_nhi_phan(mang,x)
    if vitri != -1:
        print(f'Đã tìm thấy {x} ở vị trí {vitri}')
    else:
        print('Không tìm thấy')
#[4,5,9,10] 
if __name__ == "__main__":
    main()