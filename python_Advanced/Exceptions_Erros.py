# a = 5 print(a) (Syntax error)
# a = 5 + '10'(type error)
# f = open('file.txtx') (FileNotFoundError)

# a = [1,2,3]
# a.remove(4)
# print(a) ("valueError")

# x = -5
# if x <0:
#     raise Exception("x should be positive")

# x = 5
# assert (x>=0), 'x is not positive'

# try:
#     a = 5/0
# except:
#     print("ssssssssss")

try:
    a = 5/0
    b = a + 5
except ZeroDivisionError as e: 
    print(e)
except TypeError as e: 
    print(e)
else: 
    print('everything is fine')
finally: 
    print('cleaning up...')

