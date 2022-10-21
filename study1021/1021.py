# name = "pdj"

# print (name)
# 주석처리는 crtl + /
# git init는 저장소 실행 명령어 

# print ("hello world")

# 튜플 (불변) , 리스트 [가변]
# 코딩 도장, 위키 닥스 , 파이썬 docs

# 정수 처리

# num = 
# num = 1 + 2 (3)
# num = 2 / 3 # (0.6666666666666666) x 와 y 의 몫
# num = 2 // 3 (0) 	x 와 y 의 정수로 내림한 몫
# num = 2 - 3 (-1)
# num = 1 * 5 (5)
# num = 1 % 3 (1) x / y 의 나머지
# num = -1 (-1)
# num = abs(-200) x 의 절댓값 또는 크기
# num = float(2) (2.0) 실수로 변환된 x
# num = int(-1.7) 정수로 변환된 x
# num = divmod(4, 2) # x 와 y 의 정수로 내림한 몫 과 x / y 의 나머지
# num = pow (2,4) x 의 y 거듭제곱
# num = 0.02 ** -9.5 

# import math

# num = math.trunc(8/3) x 는 Integral 로 잘립니다 <정수의 값만 들고감>
# num = math.floor(9) # 실수를 내림 할 때는 math.floor( ) 함수를 사용한다. floor는 바닥을 의미하며 실수의 바로 아래 정수를 반환한다.
# num = math.ceil(0.08)
# num2 = math.ceil(2) 실수를 올림 할 때는 math.ceil( ) 함수를 사용한다. ceil은 천장을 의미하며 실수의 바로 위 정수를 반환한다.
# from decimal import Decimal
# from unicodedata import decimal


# num = Decimal('1.5') + Decimal('0.9')

# print (num)

#문자열 처리
# name = "pdj"
# age = 23

# print("내 이름은 : " + name, "내 나이는 : " + str(age)) # 문자열과 함수는 같은열에 있을 수 없다.


# print(f"내 이름은 : {name}, 내 나이는 : {age}") # f = format은 재설정이라는 뜻

# print("내 이름은 : %s" "내 나이는 : %d"% (name, age))
# print(f"내 이름은 : {0}, 내 나이는 : {1}", format(n=name,a=age))



# 리스트 처리

# my_list = [1,2,3,4]

# print(my_list)

# for i in my_list : # for 반복문
#     print(i)

from ast import Num
import string
from tabnanny import check

# my_list = [1,2,3,4]

# my_list[0] = 9

# print (my_list)

# list는 가변이므로 중간에 수정하여도 값이 수정될수있다.

# string = "가나다라 마바사" str은 불변객체이다.

# char_list = string.split(' ') => 불변
# split은 문자열 쪼개기

# print(char_list) 

# change_string = string.replace('가', '나')

# print (id(string))
# print (id(change_string))

# list1= [1,2,3]
# list2= [1,2,3]

# print (id(list1))
# print (id(list2))
# 같은 데이터는 똑같이 취급을 해준 *숫자와 문자열에만 해당된다.
# change

# print(chain.string) 

# myList 스네이크

# Mylist 파스칼

# 조건문

# if문

# data = int(input())


# if data == 1 :
#     print("1이다")
# elif data == 2 :
#     print("2다")
# elif data == 3 :
#     print("3다") 
# elif data == 4 :
#     print("4다") 
# elif data == 5 :
#     print("5다")     
# else:
#     print("모르겠다")
    
# data = int(input())


# while 반복문

# x = 1
# while x < 10:
#     print("가나다")
#     x = x + 1
    
    # if x >= 10:
    #     break
    # else:
    #     x = x + 1
# for 반복문
    
# for list in [1,2,3,4] :
#     print(list)
      
# data = int(input())
    
# def check_data():
#     print("가나다")         
#     if check_data == 1 :
#         print("1이다")
#     elif check_data == 2 :
#         print("2다")
#     elif check_data == 3 :
#         print("3다") 
#     elif check_data == 4 :
#         print("4다") 
#     elif check_data == 5 :
#         print("5다")     
#     else:
#         print("모르겠다")
                     
# check_data()             

# while True :
#     check_data()

def sum_two_Num(n1, n2):
    return n1 + n2
    
sum_num = sum_two_Num(1, 2)
# sum_num = 3 리턴을 해주기때문에 결국에는 같은 값이다.
print(sum_num)    