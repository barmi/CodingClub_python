#### 2장 답

# Idea 3
# 임의 속담 생성 앱

from tkinter import *
import random

# 키 입력 함수:
def click():
    entered_text = entry.get()  # 텍스트 엔트리 위젯으로부터 입력한 텍스트를 수집
    output.delete(0.0, END)  # 텍스트 박스 내용 지움
    try:
        answer = my_flashcards[entered_text]
    except:
        answer = "입력한 단어가 엔트리에 없습니다."
    output.insert(END, answer)

def click1():
    questions = list(my_flashcards.keys()) # 사전의 모든 키를 숫자 인덱스로 접근할 수 있도록 리스트에 추가합니다.
    question = random.choice(questions) # 질문을 임의로 고릅니다
    entry.delete(0, END)  # 질문 입력 텍스트 박스 내용 비움
    output.delete(0.0, END)  # 출력 텍스트 박스 내용 비움
    entry.insert(END, question)

##### 메인:
window = Tk()
window.title("My 농담 App")

# 질문을 얻는 버튼을 추가합니다:
b='속담 얻기'
Button(window, text=b, width=10, command=click1).grid(row=0,column=0, sticky=W)

# 텍스트 엔트리 박스 생성
entry = Entry(window, width=58, bg="light green")
entry.grid(row=1, column=0, columnspan=2, sticky=W)

# 제출 버튼 추가:
b='정답 얻기'
Button(window, text=b, width=10, command=click).grid(row=0,column=1, sticky=E)

# 다른 레이블 생성
Label(window, text="\n대답:").grid(row=3, column=0, sticky=W)

# 텍스트 박스 생성
output = Text(window, width=75, height=6, wrap=WORD, background="light green")
output.grid(row=4, column=0, columnspan=2, sticky=W)

# 튜플들의 튜플:
my_flashcards = { 
    '개울 치고 가재 잡는다': '개울 청소도 하고 가재도 잡으니, 한 가지 일을 함으로써 두 가지 이익을 얻는다는 뜻.',
    '고기는 씹어야 맛이고 말은 해야 맛이다': '속에만 담아두지 말고 할 말은 시원하게 해야 일이 잘 풀린다는 뜻.',
    '공든 탑이 무너지랴': '정성을 들여 힘껏 한 일은 헛되지 않아 반드시 좋은 결과를 가져오리라는 뜻.',
    '까마귀가 검기로 속도 검겠냐': '외모만 보고 판단할 수 없음.',
    '꿩 먹고 알 먹는다': '한 번에 여러 이득을 얻음.',
    '늦게 배운 도둑이 날 새는 줄 모른다 ': '어떤 일에 늦게서야 재미를 붙이게 되면 몹시 열중한다는 뜻.',
    '말은 해야 맛이고 고기는 씹어야 맛이라 ': "무슨 일이든지 실제로 해 보는 데서 그 참맛을 알 수 있다는 말."
    }

##### 메인 반복문 실행
window.mainloop()

