# ch4_idea3.py
# 이 게임은 직접 만든 함수가 사용되었습니다. 숫자를 세는 변수가 추가되었으며 좀더 쉬운 겁니다.

import random

# 숫자 세는 변수 만들기:
counter = 1

# 숫자 세는 변수 만들기:
computer_number = random.randint(1, 10)

# is_same() 함수를 만듭니다.
def is_same(target, number):
    if target == number:
        result="Win"
    elif target > number:
        result="Low"
    else:
        result="High"

    return result

# 게임을 시작합니다.
print("Hello.\nI have thought of a number between 1 and 10.")

# 사용자가 추측한 숫자를 인수로 받아 옵니다.
guess = int(input("Can you guess it? "))

# is_same() 함수를 사용합니다.
higher_or_lower = is_same(computer_number, guess)

# 사용자가 숫자를 맞출때 까지 게임을 합니다.
while higher_or_lower != "Win":

    if higher_or_lower == "Low":
        guess = int(input("그것 보단 높습니다. 다시 생각해 보세요. "))
        counter = counter+1
    else:
        guess = int(input("그것 보단 낮습니다. 다시 생각해 보세요. "))
        counter = counter+1

    higher_or_lower = is_same(computer_number, guess)


print("정답!\n잘했습니다. 당신이 맞췄군요.", counter, "번 만에 맞췄네요.")

# 게임의 
input("\n\n\n종료하려면 리턴 키를 누르세요.")
