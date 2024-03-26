# num = int(input("enter a number: "))

# while True:
#     digital_root = 0

#     for digit in str(num):
#         digital_root += int(digit)
    
#     num = digital_root

#     if num < 10:
#         break

# print(num)

# def fun(n):
#     if n > 10:
#         return None
    
#     print(n)
#     fun(n + 1)

# fun(1)

# def digitalRoot(num):
#     dr = 0
#     for digit in str(num):
#         dr += int(digit)

#     num = dr
#     if num > 9:
#         return digitalRoot(num)

#     return dr

# dr = digitalRoot(int(input('num: ')))
# print(dr)

num = 238
dr = (num - 1) % 9 + 1
print(num)

