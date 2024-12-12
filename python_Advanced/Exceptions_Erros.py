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

# try:
#     a = 5/0
#     b = a + 5
# except ZeroDivisionError as e: 
#     print(e)
# except TypeError as e: 
#     print(e)
# else: 
#     print('everything is fine')
# finally: 
#     print('cleaning up...')

x = 0
class value(Exception):
    pass

class valuetolow(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise value('value is too high')
    if x < 5:
        raise valuetolow("value is too small",x)
    

try:
    test_value(1)
except value as e:
    print(e)
except valuetolow as e:
    print(e.message, e.value)

