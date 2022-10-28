from animal import Animal
# 상속 -> 해당 데이터 정보를 물려받는다.


class Dog(Animal):

    count = 0

    def __init__(self,
                 name: str = "멍",
                 age: int = 0
                 ):

        super().__init__(age)
        #  super() -> animal에 있는 변수를 가져온다.

        self.name = name

        Dog.count = Dog.count + 1

        return

    def eat(self):
        print(f"개 '{self.name}'이 음식을 먹었습니다.")
    # 부모에 있던 get.함수가 없다.

    @classmethod
    def get_count(cls):
        print(f"개가 {cls.count}마리 생성되었습니다.")
