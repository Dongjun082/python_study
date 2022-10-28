
# class 는 파스칼표기법
# init-> 초기화 (새로운 무엇을 만들때 사용된다.)

class baby:
    def __init__(self, name, age) -> None:
        self.name = name
        print("응애")
        # self.name 아기 이름의 필드

    def get_name(self):
        print(self.name)
        # 아기 이름을 말하는 기능

    def get_age(self):
        print(self.age)
    # self -> 자동으로 들어가는 값


new_baby = baby("aa", 2)
# 아기가 태어났다(Baby), 그건 new_baby이다
#

new_baby.get_name()

new_baby.get_age()
