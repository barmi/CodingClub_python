#### 5장 답

# 도전 3
# 함수 코드 리팩터링

from tkinter import *

import calc_functions

# 키 입력 함수:
def click(key):
    # = 버튼이 눌렸을 때 계산 수행:
    if key == "=":
        try:
            result = str(eval(display.get()))[0:10]
            display.insert(END, " = " + result)
        except:
            display.insert(END, " --> Error!")

    # C 버튼이 눌려졌을 때 display 엔트리 위젯 내용 비움:           
    elif key == "C":
        display.delete(0, END)  # display 엔트리 위젯 내용 비우

    # 상수 버튼에 대한 작업:
    elif key == constants_list[0]:
        display.insert(END, "3.141592654")
    elif key == constants_list[1]:
        display.insert(END, "300000000")
    elif key == constants_list[2]:
        display.insert(END, "330")
    elif key == constants_list[3]:
        display.insert(END, "149597887.5")

    # 함수 버튼에 대한 작업:
    elif key in functions_list:
        n=display.get()  # 현재 display 엔트리 위젯 값 수집
        display.delete(0, END)  # 현재 display 엔트리 위젯 내용 비움

        if key == functions_list[0]:
            display.insert(END, calc_functions.factorial(n))

        elif key == functions_list[1]:
            display.insert(END, calc_functions.to_roman(n))

        elif key == functions_list[2]:
            display.insert(END, calc_functions.to_binary(n))

        else:
            display.insert(END, calc_functions.from_binary(n))

    # 그 외 다른 키를 눌렀을 때 실행될 기본 동작:
    else:
        display.insert(END, key)

##### 메인:
window = Tk()
window.title("MyCalculator")

# top_row 프레임 생성
top_row = Frame(window)
top_row.grid(row=0, column=0, columnspan=2, sticky=N)

# 수정 가능한 엔트리 위젯
display = Entry(top_row, width=45, bg="light green")
display.grid()

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
for btn_text in num_pad_list:
    def cmd(x=btn_text):
        click(x)
    Button(num_pad, text=btn_text, width=5, command=cmd).grid(row=r,column=c)
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
for btn_text in operator_list:
    def cmd(x=btn_text):
        click(x)
    Button(operator, text=btn_text, width=5, command=cmd).grid(row=r,column=c)
    c = c+1
    if c > 1:
        c = 0
        r = r+1

# 상수 프레임 생성
constants = Frame(window)
constants.grid(row=3, column=0, sticky=W)

constants_list = [
'pi',   
'빛의 이동 속도 (m/s)', 
'소리의 이동 속도 (m/s)',  
'태양과의 평균거리 (km)' ]

# 반복문으로 상수 버튼 생성
r = 1
c = 1
for btn_text in constants_list:
    def cmd(x=btn_text):
        click(x)
    Button(constants, text=btn_text, width=22, command=cmd).grid(row=r,column=c)
    r = r+1

# 함수 프레임 생성
functions = Frame(window)
functions.grid(row=3, column=1, sticky=E)

functions_list = [
'factorial (!)',   
'-> roman', 
'-> binary',  
'binary -> 10' ]

# 반복문으로 함수 버튼 생성
r = 1
c = 1
for btn_text in functions_list:
    def cmd(x=btn_text):
        click(x)
    Button(functions, text=btn_text, width=13, command=cmd).grid(row=r,column=c)
    r = r+1

##### 메인 반복문 실행
window.mainloop()
