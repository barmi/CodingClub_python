#### 2장 답

# Idea 2
# 어휘 테스트 앱

from tkinter import *
import random

# 키 입력 함수:
def click():
    entered_text = entry.get()  # 텍스트 엔트리 위젯으로부터 입력한 텍스트를 수집
    output.delete(0.0, END)  # 텍스트 박스 내용 지움
    try:
        answer = my_flashcards[entered_text]
    except:
        answer = "단어의 정의를 찾을 수 없습니다."
    output.insert(END, answer)

def click1():
    questions = list(my_flashcards.keys()) # 사전의 모든 키를 숫자 인덱스로 접근할 수 있도록 리스트에 추가합니다.
    question = random.choice(questions) # 질문을 임의로 고릅니다
    entry.delete(0, END)  # 질문 입력 텍스트 박스 내용 비움 (이 입력 상자에는 열이 없고 0이 아니라 0.0으로 입력합니다.)
    output.delete(0.0, END)  # 출력 텍스트 박스 내용 비움
    entry.insert(END, question)


##### 메인:
window = Tk()
window.title("My Korean Vocab App")

# 질문을 얻는 버튼을 추가합니다:
b='질문 얻기'
Button(window, text=b, width=10, command=click1).grid(row=0,column=0, sticky=W)

# 다음 질문을 얻는 버튼을 추가합니다:
b='다음 질문'
Button(window, text=b, width=10, command=click1).grid(row=0,column=1, sticky=E)

# 텍스트 엔트리 박스 생성
entry = Entry(window, width=20, bg="light green")
entry.grid(row=1, column=0, columnspan=2, sticky=W)

# 정답 버튼 추가:
b='정답 얻기'
Button(window, text=b, width=10, command=click).grid(row=3,column=0, sticky=W)

# 텍스트 박스 생성
Label(window, text="\n정답:").grid(row=5, column=0, sticky=W)

# create text box
output = Text(window, width=75, height=6, wrap=WORD, background="light green")
output.grid(row=6, column=0, columnspan=2, sticky=W)

# 사전:
my_flashcards = { 
    'school': "학교",
    'cat': '고양이',
    'bridge': '다리',
    'ghost': '유령',
    'house': '집'
    }

##### 메인 반복문 실행
window.mainloop()

