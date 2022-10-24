def isInvalidUrl(url = "www.naver.com"):
    print(url, "is invalid")

isInvalidUrl()

def sum(arg1, arg2):
    res = arg1 + arg2;
    return res

def sumZero(a, b):
    print(a + b)

a = sum(10000, 5)

b = sum(0, 5000)

a = sum("1234", "5")
print(a)
#b = a + 3 타입이 틀리면 연산불가능한 듯?
print(b)
#sumZero(a, 0)

# Format String

my_name="JYL"
my_age="88"
my_hobby="sw"
formated_string = f"Hello {my_name}! ur {my_name} {my_hobby}"
print(formated_string)

# printf가 프린트 포맷이었던거신가?!?!?

# systax error
# def funcLikeSwift(with str):
 #   print(str)
#funcLikeSwift("hello world")

a = 3
b = 3
if a > b:
    print("a over b")
elif a == b:
    print("===")
else:
    print("b over a")
