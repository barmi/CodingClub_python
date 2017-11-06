# ch4_idea1.py
# 이 게임은 직접 만든 함수를 사용합니다.

# 앱을 시작하고 선택을 고르세요.
which_table = int(input("안녕하세요.\n어느 구구단을 좋아하시나요?. 숫자를 입력하세요.:\n"))
how_many_rows = int(input("원하는 행이 몇개인가요? 숫자를 입력하세요.:\n"))

def times_tables(how_far, num):
    n=1
    while n<= how_far:
        print(n, " x ", num, " = ", n*num)
        n = n+1

# 줄 넘기기 추가
print()

# 직접 만든 함수
times_tables(how_many_rows, which_table)

# End the game# adds a line return
input("\n\n종료하려면 리턴 키를 누르세요.")
