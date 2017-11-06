# 빠르게 살펴보는 Ch1-Idea2.py 프로그램.

import random

# 변수 초기화:
response1 = "걱정말고 다시 시도해보세요."
response2 = "그럴듯하지만 내 비밀번호는 아니에요. 다시 입력해보세요."
response3 = "내 비밀번호가 아니에요. 내 비밀번호는 정말 쉬워요."
response4 = "잘했어요!"
MY_PASSWORD = "내 비밀번호에요"

# 3개의 새로운 변수:
guess_correct = False
counter = 0
gave_in = False

def is_correct(guess, password):
    return guess == password

# 게임 시작:
print("안녕.\n")
users_guess = input("추측한 내 비밀번호를 입력하세요. ")

# 함수를 사용하여 입력한 비밀번호가 일치하는지 확인:
true_or_false = is_correct(users_guess, MY_PASSWORD)

# 사용자가 입력한 비밀번호가 일치할 때까지 게임 실행:
while true_or_false == False:
    computer_response = random.randint(1, 3)

    # 세 번째 시도 확인:
    if counter >= 2:
        yes_or_no = input("포기하시겠습니까? Y/N? ")
        if (yes_or_no == "Y" or yes_or_no == "y"):
            print("내 비밀번호가 \"my password\"에 있습니다. 확인하시겠어요?")
            gave_in = True
            break
        else:
            print("\n좋아요. 계속 하겠습니다. ...")

    if computer_response == 1:
        print(response1)
    elif computer_response == 2:
        print(response2)
    else:
        print(response3)

    # 사용자에게 다시 시도할 비밀번호 입력 요청:
    users_guess = input("\n다음 비밀번호는 무엇입니까? ")

    # 비밀번호가 일치하는지 재확인:
    true_or_false = is_correct(users_guess, MY_PASSWORD)

    # 카운터에 1을 추가:
    counter = counter+1

# 게임 종료:
if gave_in == False: print(response4) # 이 줄은 새로운 줄에 적을 수 있습니다
input("\n\n\n리턴 키를 눌러 끝내세요.")
