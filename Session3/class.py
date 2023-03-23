class Person:
    keyboard = "기계식"
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def introduce(self):
        print(f"저는 {self.age}살 {self.name}이고, 키는 {self.height}cm 입니다.")

    def yell(self):
        print(f"아?")

class Developer(Person):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)

    def yell(self):
        print(f"어?")

class Designer(Person):
    def __init__(self, name, age, height, disease):
        super().__init__(name, age, height)
        self.disease = disease

class ProductManager(Person):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)

    def yell(self):
        print(f"개발자님 여기 오류있어요!")

    def aging(self):
        self.age += 2
        self.height -=5
        print(f"개발자를 새로 뽑아야하나...")
        self.keyboard = "엠브레인"

d1 = Developer('김개발자', 21, 170)
d1.introduce()
d1.yell()

d2 = Designer('정디자이너', 23, 165, '없음')
d2.introduce()
d2.yell()

p1 = ProductManager('이PM', 23, 175)
p1.introduce()
p1.yell()
p1.aging()
p1.introduce()


