# myCalculator_expt1.py

from tkinter import *
from decimal import *


##### 메인:
window = Tk()
window.title("MyCalculator")

# 내용 수정이 가능한 엔트리 위젯을 사용해 결과 디스플레이 사용
display = Entry(window, width=45, bg="light green")
display.grid()

# 숫자 버튼 생성:
def click1():
    display.insert(END, "1")
    
Button(window, text="1", width=5, command=click1).grid(row=1,column=0)


##### 메인 반복문 실행
window.mainloop()
