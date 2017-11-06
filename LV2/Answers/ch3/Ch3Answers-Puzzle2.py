#### 3장 답

# 퍼즐 2
# 추가 버튼

from tkinter import *
from decimal import *

# 키 입력 함수:
def click(key):
    entry.insert(END, key)

##### 메인:
window = Tk()
window.title("MyCalculator")

# top_row 프레임 생성
top_row = Frame(window)
top_row.grid(row=0, column=0, columnspan=2, sticky=N)

# 수정 가능한 엔트리 위젯
entry = Entry(top_row, width=45, bg="light green")
entry.grid()

# 숫자 버튼 프레임 생성
num_pad = Frame(window)
num_pad.grid(row=1, column=0, sticky=W)

num_pad_list = [
'7',  '8',  '9',
'4',  '5',  '6',
'1',  '2',  '3',
'0',  '.',  '=' ]

# 반복문으로 숫자 버튼 생성
r = 1
c = 0
for b in num_pad_list:
    # 이 부분은 나중에 수정될 것입니다:
    Button(num_pad, text=b, width=5, command=click).grid(row=r,column=c)
    c = c+1
    if c > 2:
        c = 0
        r = r+1

# 연산자 프레임 생성
operator = Frame(window)
operator.grid(row=1, column=1, sticky=E)

operator_list = [
'*', '/',  
'+', '-',
'(', ')',
'C' ]

# 반복문으로 연산자 버튼 생성
r = 2
c = 0
for b in operator_list:
    Button(operator, text=b, width=5, command=click).grid(row=r,column=c)
    c = c+1
    if c > 1:
        c = 0
        r = r+1

# bottom_row 프레임 생성
bottom_row = Frame(window)
bottom_row.grid(row=2, column=0, columnspan=2, sticky=S)

# 게임 버튼 생성   
wide_button=Button(bottom_row, text="나의 추가 버튼", width=43, command=click)
wide_button.grid()

##### 메인 반복문 실행
window.mainloop()
