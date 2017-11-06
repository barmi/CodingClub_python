# pet.py가 제공하는 강화된 Cat 클래스

class Pet:
    # 생성자
    def __init__(self, name):
        self.name = name

    # 기타 메서드
    def sleep(self):
        print(self.name, "가 잠을 잡니다.")

    def eat(self):
        print(self.name, "가 약간의 음식을 먹습니다.")
        print(self.name, "가 조금 더 음식을 원합니다.")
