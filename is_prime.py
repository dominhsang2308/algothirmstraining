
# def is_prime():
    
#     for i in range(2,100):
#         is_prime = True
#         for j in range(2,i):
#             if i % j == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(i)   

# is_prime()

#C -> F temputure

def temputure():
    print('1. Chuyển từ độ C sang độ F ')
    print('2. Chuyển từ độ F sang độ C ')
    user_choice = input('Vui lòng chọn 1 trong 2 ')

    if user_choice == '1':
        c_temputure = float(input('Nhập nhiệt độ C : '))
        f_temputure = (c_temputure * 9/5) + 32
        print(f'{c_temputure} độ C chuyển sang = {f_temputure}')
    elif user_choice == '2':
        f_temputure = float(input('Nhập nhiệt độ F : '))
        c_temputure = (f_temputure - 32 ) * 5/9
        print(f'{f_temputure} độ F chuyển sang C = {c_temputure}')
    else:
        print('Lựa chọn không hợp lệ ')

temputure()