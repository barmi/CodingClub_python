# myCalculatorPlus.py
# 대체 게임을 포함한 계산기

from tkinter import *
import calc_functions

import time
import random

# 게임 변수 초기화:
target = random.randint(0, 9)
start_time = 0
counter = 0
game_state = "not_playing" # 다른 상태: "진행중"이거나 "기다리는 중" 등 열심히 게임을 시도하는 상태가 있습니다
choice=0

# key press function:
def click(key):
    global target
    global counter
    global choice
    global start_time
    global game_state
    
    # = 버튼이 눌렸을 때 계산 수행:
    if key == "=":
        try:
            result = str(eval(display.get()))[0:10]
            display.insert(END, " = " + result)
        except:
            display.insert(END, " --> 오류!")

    # C 버튼이 눌려졌을 때 display 엔트리 위젯 내용 비움:           
    elif key == "C":
        display.delete(0, END)

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
        n = display.get()  # 현재 display 엔트리 위젯 값 수집
        display.delete(0, END)  # 현재 display 엔트리 위젯 내용 비움

        if key == functions_list[0]:
            display.insert(END, calc_functions.factorial(n))

        elif key == functions_list[1]:
            display.insert(END, calc_functions.to_roman(n))

        elif key == functions_list[2]:
            display.insert(END, calc_functions.to_binary(n))

        else: 
            display.insert(END, calc_functions.from_binary(n))

    # 다른 버튼이 눌리면 현재 항목의 끝에 값을 추가합니다:

    #### 진행 시간 ####
    elif key == "play": # game_button이 눌렸을때 게임을 시작합니다.


        if game_state == "not_playing":
            display.insert(END, "연습할 시간 테이블을 선택하고 시작하세요:")
            game_button["text"] = "시작"
            game_state = "waiting"      
                
        elif game_state == "waiting":
            try:
                choice=int(display.get()[51:]) # 메시지를 제거하고 새로운 숫자를 얻습니다.
                game_button["text"] = "정지"
                target=random.randint(0, 9)
                big_target=target*choice
                display.delete(0, END)
                display.insert(END, big_target)
                game_state = "playing"
                start_time=time.time()
            except:
                display.insert(END, " --> 오류!")
                game_state = "not_playing"

        else: # game_state == "playing"와 같을 때 플레이어가 게임을 종료하려고 할때 수행합니다.
            game_button["text"] = "진행 시간"
            display.delete(0, END)
            counter=0
            game_state = "not_playing" 

    elif game_state == "playing": # 게임을 진행하고 있을 때
        if key.isdigit() and key == str(target): 
            display.delete(0, END)  # display 엔트리 위젯 내용 비움
            target=random.randint(0, 9)
            big_target=target*choice
            display.insert(END, big_target)
            counter=counter+1
            if counter==10:
                display.delete(0, END)
                achieved_time=(time.time()-start_time)
                achieved_time=str(achieved_time)[:5] # # 문자열의 5자리까지만 잘라냅니다.
                message="잘했습니다. 10번 중 " + achieved_time + "번 만에 성공하셨습니다"
                display.insert(END, message)
                counter=0
                game_button["text"] = "진행 시간"
                game_state == "not_playing"
            
        else:
            display.insert(END, " whoops!")

    #### 진행 시간을 초과했을 때
 
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
r = 0
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
r = 0
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
r = 0
c = 0
for btn_text in constants_list:
    def cmd(x=btn_text):
        click(x)
    button=Button(constants, text=btn_text, width=22, command=cmd).grid(row=r,column=c)
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
r = 0
c = 0
for btn_text in functions_list:
    def cmd(x=btn_text):
        click(x)
    Button(functions, text=btn_text, width=13, command=cmd).grid(row=r,column=c)
    r = r+1

# bottom_row 프레임 생성
bottom_row = Frame(window)
bottom_row.grid(row=10, column=0, columnspan=2, sticky=S)

#  game 버튼 생성
def cmd(x="play"):
    click(x)   
game_button=Button(bottom_row, text="진행 시간", width=43, command=cmd)
game_button.grid()


##### 메인 반복문 실행
window.mainloop()
