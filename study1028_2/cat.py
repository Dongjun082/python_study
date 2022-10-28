from animal import Animal
# 상속 -> 해당 데이터 정보를 물려받는다.


class Cat(Animal):

    count = 0

    def __init__(self,
                 name: str = "냥",
                 age: int = 0
                 ):
        """

        Args:
            name (str, optional): 고양이의 이름. 기본값은 "냥".
            age (int, optional): 고양이의 나이. 기본값은 0.
        """

        super().__init__(age)
        #  super() -> animal에 있는 변수를 가져온다.

        self.name = name

        Cat.count = Cat.count + 1

        return

    def eat(self):
        print(f"고양이 '{self.name}'이 음식을 먹었습니다.")
    # 부모에 있던 get.함수가 없다.

    @classmethod
    def get_count(cls):
        print(f"고양이가 {cls.count}마리 생성되었습니다.")
