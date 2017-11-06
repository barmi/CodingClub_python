#### 2장 답

# 도전
# 퀴즈 앱

#######################################################################################
# 이번 도전에서는 텍스트 박스의 내용을 변경함으로서 발생하는 버그를 수정할 필요가 있습니다                #
# 프로그램의 실행 결과로 "찾고자 하는 단어가 없습니다"가 계속 발생될 수 있습니다.                      #
#                                                                                     #
# 이 오류를 추적하는 한가지 방법은 오류 메시지 표시를 제거하거나 try와 except로 감싸 오류 메시지를 보여주는#
# 것입니다. 에러 메시지는 다음과 같습니다.                                                     #
#                                                                                     #
# KeyError: '데이터 타입은 무엇인가요?\n'                                                   #
#                                                                                     #
# get(0.0, END)와 같이 END를 사용하면 입력값 및 예상되는 결괏값을 수집할 수 있습니다.               #
# 이 문제에 해결 방법은 다음과 같은 것이 있습니다.                                              #
# 1. rstrip() 함수를 사용해 줄의 가장 우측에 있는 \n을 제거합니다.                               #
# 2. 첫번째 라인만을 수집하도록 get(0.0, 1.75)를 사용합니다.(첫 번째 라인으로 최대 75자를 가지고 옵니다)#
# 3. question 변수를 전역 변수로 만듭니다(이 예제에서 솔루션으로 사용되었습니다)                     #
#######################################################################################

from tkinter import *
import random

question = ""

# 키 입력 함수:
def click():
    output.delete(0.0, END)  # 출력 텍스트 박스 내용 비움
    try:
        answer = my_flashcards[question]
    except:
        answer = "입력한 단어를 찾을 수 없습니다."
    output.insert(END, answer)

def click1():
    global question # 함수 바깥에서 선언한 변수의 값을 변경할 수 있도록 전역 변수로 선언합니다.
    questions = list(my_flashcards.keys()) # 사전의 모든 키를 숫자 인덱스로 접근할 수 있도록 리스트에 추가합니다.
    question = random.choice(questions) # 질문을 임의로 고릅니다
    entry.delete(0.0, END)  # 질문 입력 텍스트 박스 내용 비움
    output.delete(0.0, END)  # 출력 텍스트 박스 내용 비움
    entry.insert(END, question)

##### 메인:
window = Tk()
window.title("My Quiz App")

# 질문을 얻는 버튼을 추가합니다:
b='질문 얻기'
Button(window, text=b, width=10, command=click1).grid(row=0,column=0, sticky=W)

# 질문 얻기 버튼을 추가합니다:
b='다음'
Button(window, text=b, width=10, command=click1).grid(row=0,column=1, sticky=E)

# 텍스트 엔트리 박스 생성
entry = Text(window, width=75, height=1, wrap=WORD, background="light green")
entry.grid(row=1, column=0, columnspan=2, sticky=W)

# 제출 버튼 추가:
b='정답 얻기'
Button(window, text=b, width=10, command=click).grid(row=3,column=0, sticky=W)

# 다른 레이블 생성
Label(window, text="\n정답:").grid(row=5, column=0, sticky=W)

# 텍스트 박스 생성
output = Text(window, width=75, height=6, wrap=WORD, background="light green")
output.grid(row=6, column=0, columnspan=2, sticky=W)

# 사전:
my_flashcards = {
    '인수는 무엇인가요?': '작업을 수행할 수 있는 함수에 의해 요구되는 정보의 조각. 보통 문자 또는 숫자가 사용되며 my_function(인수)와 같이 사용합니다.',
    '2진수는 무엇인가요?': '2진법으로 나타낸 숫자',
    '버그는 무엇인가요?': '프로그램이 적절하게 동작하는 데 실패하거나 또는 전혀 동작하지 않는 원인을 제공하는 코드 조각',
    '형변환은 무엇인가요?': '어떤 자료형을 다른 자료형으로 변환하는 과정. 예를 들면 때때로 번호가 문자 형식인 경우 숫자 형식으로 변환할 필요가 있을 때 다음과 같이 사용하여 변환합니다. int("3")',
    '주석은 무엇인가요?': '컴퓨터 프로그램에 적는 텍스트로서 사람이 읽으며 프로그램 실행중에 컴퓨터가 무시합니다. 파이썬에서 모든 주석은 해시 기호(#)로 시작합니다.',
    '비교 연산자는 무엇인가요?': '때때로 프로그램의 데이터를 비교할 수 있도록 논리 연산자를 호출합니다. 이 연산자는 ==, > 연산자를 포함합니다.',
    '상수는 무엇인가요?': '변경되지 않는 수. 상수의 이름을 대문자로 이름 짓는 것은 좋은 습관입니다. 예: SPEED_OF_LIGHT',
    '컨테이너는 무엇인가요?': '컨테이너 자료형은 여러 자료형을 그룹지어 저장하는 자료형이며 여러 컨테이너를 포함할 수 있습니다. 컨테이너 자료형은 튜플, 리스트와 사전에서 사용됩니다.',
    '데이터 타입은 무엇이 있나요?': '컴퓨터에 저장된 다른 정보의 형태로서 예를 들어 실수, 정수, 문자열, 튜플, 리스트와 사전이 있습니다.',
    '디버깅은 무엇인가요?': '프로그램의 버그를 찾는 과정'
    }

##### 메인 반복문 실행
window.mainloop()
