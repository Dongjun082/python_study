# 문자열

temp = "abc"
# 문자열은 요소를 번호로 가져올 수 있다.
# temp[0]='a'


# temp[0] = 'd'
# 문자열은 불변이라 요소를 변경할 수 없다.
# TypeError: 'str' object does not support item assignment

temp = "d"
# 변수에 다른 문자열을 넣을 수는 있다.
# 불변 temp라는 값을 d에다가 붙여줌 원래 있던 변수는 존재는 하지만 없는 잉여자원이 된다

del temp
# 변수를 삭제한다.
# NameError: name 'temp' is not defined

temp = "abc"
temp = "b"
temp = "abc"

# 문자열, 숫자는 메모리 어딘가에 저장되어 다시 불러와진다.
# 파이썬 할당
# id(temp)=2221146087152
# id(temp)=2221145969264
# id(temp)=2221146087152

temp = "가나다\n라마바"
# 문자열을 여러줄로 출력하고 싶으면 \n 사용한다.
# 가나다
# 라마바

temp = """
가나다
마바사
"""
# 가나다
# 마바사

temp = "그가 말했다." '"안녕하세요"'
# 쌍따음표를 문자열 안에 넣고 싶을 때 홑 따옴표로 감싼다.
# 그가 말했다."안녕하세요"

temp = "나는 생각했다. '잠온다'"
# 나는 생각했다. '잠온다'

temp = """그가 말했다. "안녕하세요" 나는 생각했다. '잠온다'"""
# 쌍따옴표 홑따옴표 모두 넣을 경우 """ 또는 ''' 를 사용한다.
# 그가 말했다. "안녕하세요" 나는 생각했다. '잠온다'

temp = temp[0:3]
# 시퀀스는 대괄호를 사용해서 불러낼수있다.
# 그가


temp = "가나다라"
temp = temp[-1]
# temp='라'

# temp = temp[4]
# 범위를 넘는 요소 번호를 호출하면 에러가 발생한다.
# IndexError: string index out of range

temp = "가나다라"
temp = temp[-4]
# temp='가'

temp = "가나다라"
# temp = temp[-5]
# 범위를 벗어나서 에러

temp = "가나다라"
temp = temp[1:]
# 1번지부터 끝까지 호출한다.
# temp='나다라'

temp = "가나다라"
temp = temp[:2]
# temp='가나'

temp = "가나다라"
temp = temp[1:100]
# temp='나다라'
# 파이썬은 문자열 컷팅은 유연하다.

temp = "가나다라"
temp = temp[5:100]
# temp=''

temp = "가나다라"
temp = temp[-100:100]
# temp='가나다라'
# 지정해준 숫자값이 없다라도 어떤식으로든 지정된 값이 아니더라도 호출해준다.
# for item in temp:
#     print(temp)

temp = ("가나" +
        "다라" +
        "여러글" +
        "쓰고싶어요")
# temp='가나다라여러글쓰고싶어요'

# temp = len(temp)
# 문자열의 길이를 알고싶으면 len 함수를 사용한다.
# temp=12

temp = temp[len(temp)-1]
# temp='요'

temp = "가나다라"

temp = f"한글은 {temp}"
# temp='한글은 가나다라'
# f"" f'' 를 이용해서 변수를 문자열에 입력할 수 있다.

temp = "가나다라"

temp = "한글은 " + temp
# temp='한글은 가나다라'

temp = "가나다라"

temp = "한글은% s " % temp
# temp='한글은가나다라 '

temp = "가나다라"

temp = "한글은{0}".format(temp)
# temp='한글은가나다라'

temp = "가나다라"

temp = "한글은{arg1}".format(arg1=temp)
# temp='한글은가나다라'

temp = "가나다라"
temp = temp.startswith("다라")
# temp=True
# temp=False
# 문자열의 시작을 확인하여 True Flase로 확인한다.

temp = "가나다라"
temp = temp.endswith("다라")
# temp=True
# 스타트와 반대 되는 스위치

temp = "가나다라"
temp = temp.index("가")
# index = 해당되는 문자열의 요소 번호(번지)를 확인시켜준다.

temp = "1"
temp = temp.zfill(2)
# temp='01'
# 빈자리수를 0으로 채워준다.

temp = "1"
temp = temp.rjust(5, "0")
# temp='00001'
# rjust = 내가 원하는 문자로 채워 줄 수있다.


print(f"{temp=}")
