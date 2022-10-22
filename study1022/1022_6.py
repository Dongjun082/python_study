# 예약어

from logging import exception
from math import pow
# from math import pow
# math에서 pow라는 함수를 가져올것이다.
# as는 별명을 지어주는것이다.

# is = "aa"

# temp = None
# print("temp = " + str(temp))
# temp = True and False

# assert False
# 반복문이나 디버그 확인용으로 사용가능

# print(temp)
# temp
# name 'temp' is not defined 파이썬에서는 지정을 해줘야 한다.

# for item in range(10):
#     # 처음
#     if item == 5:
#         # 반복문의 처음으로 돌아간다.
#         continue
#     elif item == 8:
#         # 반복문을 멈춘다.
#         break

#         print(item)


# try:
#     temp = "가나다"
#     temp[0] = "마"
# except exception as e:
#     print(e)
#     e.with_traceback()
#     print("에러가 발생했습니다.")
# finally:
#     print("마지막으로 할 것은 하겠습니다.")

# print("넘어왔습니다.")


# temp = 1

# for i in range(10):
#     pass

# print(temp)

# = 1


# temp = 1

# for temp in range(10):
#     pass

# print(temp)

# = 9


temp = 1


# def my_func():
#     global temp
#     temp = 3
#     return temp


# print(my_func())
# print(temp)
# 3 my_func()
# 1 temp
# global 함수는 지정한 범위내에 함수를 가져오는것

# raise Exception("내가 만든 에러")
# 본인이 직접 생성한 에러

# 파라미터
# def my_func(num):
#     print(num)


# my_func(12)
# 아규먼트, 인자, 함수

#  def my_func(num): return print(num)


# my_func(12)

# lambda 익명 함수를 만드는 연산자.

# temp = list(filter(lambda num: num != 1, [1, 2, 3, 1]))

# print(temp)


# yield

# def my_func():
#     while True:
#         yield 1
#         yield 2
#         yield 3


# my_yield_data = my_func()

# for item in my_yield_data:
#     print(item)

# print(next(my_yield_data))
# print(next(my_yield_data))
# print(next(my_yield_data))
# print(next(my_yield_data))

# yield (while)을 함께 사용하여 무한반복이 가능하다.
# 데이터 또는 함수를 넣어서 원하는 횟수만큼 사용이 가능하다.


def check_str(data: str):
    return data.endswith("마")


print(check_str("가나다"))
