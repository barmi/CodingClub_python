# cat2.py가 제공하는 강화된 Cat 클래스

class Cat:
    # 생성자
    def __init__(self, name):
        self.name = name

    # other methods
    def speak(self):
        print(self.name, "가 야옹합니다.")

    def drink(self):
        print(self.name, "가 우유를 마셔요.")
        print(self.name, "가 낮잠을 잡니다.")
