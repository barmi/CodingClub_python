# ch4_idea4.py
# 이 게임은 직접 만든 함수가 사용되었습니다. 숫자를 세는 변수가 추가되었으며 레벨을 선택할수 있습니다.

import random

# 숫자 세는 변수 만들기:
counter = 1

# is_same() 함수를 만듭니다.
def is_same(target, number):
    if target == number:
        result="Win"
    elif target > number:
        result="Low"
    else:
        result="High"

    return result

# 어떤 레벨을 선택할 것인지 사용자게 물어봅니다.:
level = input("안녕하세요.\n어떤 게임을 할지 고르세요: 쉬움, 중간 또는 어려운거?\ne/m/h:")

while level != "e" and level != "m" and level != "h":
    level = input("죄송합니다. 엉뚱한 글자를 입력하셨네요. 다음 글자중에 하나를 골라야 합니다. 'e', 'm' or 'h'\ne/m/h:")

# 레벨 선택
if level == "e":
    upper_limit = 10
elif level == "m":
    upper_limit = 20
else:
    upper_limit = 100
    
# 맞힐 숫자를 만듭니다.
computer_number = random.randint(1, upper_limit)

# 게임을 시작합니다.
print("\nI have thought of a number between 1 and ", upper_limit)

# 사용자가 추측한 숫자를 인수로 받아 옵니다.
guess = int(input("Can you guess it? "))

# is_same() 함수를 사용합니다.
higher_or_lower = is_same(computer_number, guess)

# 추측
while higher_or_lower != "Win":

    if higher_or_lower == "Low":
        guess = int(input("그것 보단 높습니다. 다시 생각해 보세요. "))
        counter = counter+1
    else:
        guess = int(input("그것 보단 낮습니다. 다시 생각해 보세요. "))
        counter = counter+1

    higher_or_lower = is_same(computer_number, guess)


print("정답!\n잘했습니다. 당신이 맞췄군요.", counter, "번 만에 맞췄네요.")

# 게임 끝
input("\n\n\n종료하려면 리턴 키를 누르세요.")
