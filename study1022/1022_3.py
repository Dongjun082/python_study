# bool

from os import remove


temp = True
temp = False
temp = 10 > 1
temp = "가나다".startswith("가")
# temp = [1,2,3].index{1} int의 값을 return 시킨다.

# if temp :
#     print("")

temp = None
# 일방적으로 null, nil의 값은 없는 데이터이다.
# 파이썬에서는 None이 없음으로 처리된다. , 파이썬은 객체지향언어이다.
# none 과 false 거짓으로 정의된 상수
# 파이썬 라이브러리 참고


if None:
    print("?")
else:
    print("f")


# 예시 (bool)

# def asdf():
#     return True


# list


temp = [1, 2] + [3, 4]
temp.append(5)
# append 값을 추가 해주는 명령문
temp.remove(1)
# remove 값을 삭제 해주는 명령문

# temp = [1, 1, 1, 1]
# temp.remove(1)
# [1, 1, 1]
# 모든 같은 데이터를 지우지를 못한다. 하나의 데이터만 지운다.

temp = [1, 1, 1, 1]


def check(num):
    if num == 1:
        return False
    else:
        return True


# print(check(12321312))
# print(True)

temp = [1, 2, 3, 1, 1]
temp = filter(check, temp)
temp = list[temp]

# temp = list(filter(check, [1, 1, 1, 1]))

print(temp)

temp = 1  # 0차원 리스트
temp = [1, 2, 3, 4, 5]  # 1차원 리스트
temp = [
    [1, 2],
    [3, 4]
]
# 2차원 리스트
# [0]번지는 1행
# [1]번지는 2행
# []이 늘어날수록 차원도 늘어난다.

# print(temp[0])
# print(temp[1])


temp = [
    (1, 2),
    (3, 4)
]

# set
temp = [
    {"1", "2"},
    {"3", "4"}
]

# 딕셔너리
temp = [
    {"key ": "value", "name": "이름"},
    {"aa": "dd", "cc": "hg"}
]

print(temp[0]["name"])
