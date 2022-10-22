# 정수 계산
# 파이썬 프롬프트가 나오면 코드와 계산식을 입력받을 준비가 된 상태입니다.
print(1 + 1)
# 위와 같이 사칙연산이 가능하다.
# 하지만 파이썬은 저웃끼리 나눗셈을 해도 실수가 나온다는것
print(4 / 2)
# 완벽히 나누어 떨어져도 파이썬은 실수로 처리가 된다.
# import math 수학 함수
# c 표준으로 정의된 수학 함수를 제공하며, 달리 명시는 안되지만 모든값은 float(실수)로 반영된다.

# 문자열 처리
name = "pdj"
age = 23
print("내 이름은 : " + name, "내 나이는 : " + str(age))
# 문자열과 함수는 같은열에 있을 수 없다.
# 따라서 함수인 age에 str으로 변경시켜야 대입가능
print(f"내 이름은 : {name}, 내 나이는 : {age}")
# f = format은 재설정이라는 뜻 f({})에 지정값을 넣으면 원래 넣었던 값으로 출력된다.
print("내 이름은 : %s" "내 나이는 : %d" % (name, age))
# %s는 문자열, %d는 인수이다.
print(f"내 이름은 : {0}, 내 나이는 : {1}", format(n=name, a=age))
# format으로 name, age를 지정해주어 0, 1에 각각  n, a가 들어가게된다.

# 리스트 처리

my_list = [1, 2, 3, 4]
# 리스트는 가변형이여서 자유롭게 변경이 가능하다.
my_list[0] = 9
# 위와 같이 0번지에 9란 숫자를 넣으면 출력시 9,2,3,4으로 출력이 된다.
# 다만 string = "가나다라 마바사" str, char은 불변객체이다.
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(id(list1))
print(id(list2))
# 같은 데이터는 똑같이 취급을 해준 숫자와 문자열에만 해당된다.
# myList 스네이크 , Mylist 파스칼로 나뉜다

# 조건문

# if문
data = int(input())

if data == 1:
    print("1이다")
elif data == 2:
    print("2다")
elif data == 3:
    print("3다")
elif data == 4:
    print("4다")
elif data == 5:
    print("5다")
else:
    print("모르겠다")

# 값을 입력하고 해당 값이 맞는 경우에 순차적으로 if들이 출력이 되고,
# 아닐 경우 else의 값이 출력이 된다. 다만 숫자가 아닌 문자 혹은 다른것이 들어간다면 에러가 생김

# while 반복문

x = 1
while x < 10:
    print("가나다")
    x = x + 1

# while은 x의 값을 지정하지않고 true라고 지정해준다면 무한반복이 된다.
# while은 값을 지정해주어야 멈추는 형식의 반복문이라고 볼수있다.

# for 반복문

for list in [1, 2, 3, 4]:
    print(list)

data = int(input())


def check_data():
    print("가나다")
    if check_data == 1:
        print("1이다")
    elif check_data == 2:
        print("2다")
    elif check_data == 3:
        print("3다")
    elif check_data == 4:
        print("4다")
    elif check_data == 5:
        print("5다")
    else:
        print("모르겠다")

# for 변수 in 리스트(또는 튜플, 문자열): 형식으로 다루어져 있다.
