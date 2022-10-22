# enumerate

from multiprocessing.sharedctypes import Value
from re import template


# temp = ("a", "b", "c")
# temp = enumerate(temp)

# for num, value in temp:
#     print(num, value)


a, d = {"name": "aa", "age": "23"}.items()
# ValueError: too many values to unpack (expected 2)
# 변수보다 데이터가 많을 경우 뜨는 에러

print(a)
print(d)
