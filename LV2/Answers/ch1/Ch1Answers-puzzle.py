#### 1장 답

# 퍼즐
#My Magic 8 Ball

import random


# 답을 리스트에 넣습니다.
answers = [
    "자! 해보세요!",
    "됐네요, 이 사람아",
    "뭐라고? 다시 생각해보세요.",
    "모르니 두려운 것입니다.",
    "칠푼인가요?? 제 정신이 아니군요!",
    "당신이라면 할 수 있어요!",
    "해도 그만, 안 해도 그만, 아니겠어요?",
    "맞아요, 당신은 올바른 선택을 했어요."
    ]

print("MyMagic8Ball에 오신 것을 환영합니다.")


# 사용자의 질문을 입력 받습니다.
question = input("조언을 구하고 싶으면 질문을 입력하고 엔터 키를 누르세요.\n")

print("고민 중 ...\n" * 4)

# 질문에 알맞은 답변을 하는 일에 randint() 함수를 활용합니다.
choice=random.randint(0, 7)

# 화면에 답변을 출력합니다.
print(answers[choice])

# 이제 종료합니다.
input("\n\n마치려면 엔터 키를 누르세요.")
