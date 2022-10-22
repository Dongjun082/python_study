import math
from unicodedata import decimal
# 파이썬이 가지고 있는 기본적인 라이브러리다.
# 표준라이브러리

temp = 1 + 2 * 3
# 연산자에게는 순서가 없다
# 예) * 가 + 보다 우선이다.
# temp = 7

temp = (1+2) * 3
# 연산 우선순위를 바꾸기 위해 ()를 사용한다.
# temp = 9

# temp = 1 / 0
# ZeroDivisionError: division by zero
# 숫자는 0으로 나눌 수 없다.

temp = 1.1 + 0.1
# 실수 중에서 2진수로 계산할 수 없는 숫자는 근사값만 나온다.
# temp = 1.2000000000000002

# temp = decimal('1.1') + decimal('0.1')
# temp = float(temp)
# decimal을 사용하면 정재된 실수 값을 계산할수 있다. 하지만 자리수가 한정 되어 있다.
# temp = 1.2

temp = 11
temp = bin(temp)
# bin을 사용하면 2진수로 바꿀 수 있다.
# temp = 0b1011

temp = 11
temp = oct(temp)
# bin을 사용하면 8진수로 바꿀 수 있다.
# temp = 0o13

temp = 11
temp = hex(temp)
# hex를 사용하면 16진수로 바꿀 수 있다.
# temp = 0xb
# 16진수는 = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f
# (a = 10)...(f = 15)

print(f"{temp}")
