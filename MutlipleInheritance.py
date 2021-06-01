class A:
    def method1(self):
        print("Class A and MethodA")


class B:
    def method1(self):
        print("Class B and MethodB")


class C(B, A):
    # def method1(self):
    print("Class C and MethodC")


Obj = C()
# obj.methodC
Obj.method1()


# yield keyword will have ability to convert any function to Generator and returns the object values'
def fun(n):
    a, b = 0, 1
    for j in range(0, n):
        a, b = b, a + b
        # print("after assignment:: ",a,b)
        # a=b
        # b=a+b
        yield a


for i in fun(5):
    print(i)


# global variable
def a():
    # b = 10
    global b
    b = 1


def b1():
    a()
    print("Value", b)


# try except else finally
def divide(x,y):

    try:
        r= x /y
    except Exception as e:
        print("SOrry u r dividing by zero:: ",e)
    else:
        print("else",x/5)
    finally:
        print("finally")
divide(3, 2)
divide(3, 0)

# for k,v in dict.items():
#     print(k,v)

st = "raja reddy@  v!"
alphanumeric=""
cnt=""
for char in st:
    if char.isalnum():
        alphanumeric+=char
    else:
        cnt+=char

print(alphanumeric)
print("special char and space:: ",cnt)
