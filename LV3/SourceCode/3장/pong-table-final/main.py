# MyPong의 주된 파일을 만듭니다.

from tkinter import *
import table

# tkinter 공장으로부터 윈도우 주문
window = Tk()
window.title("MyPong")
       
# Table 공장으로부터 table 주문
my_table = table.Table(window, net_colour="green", vertical_net=True)

# GUI를 계속 그리는 반복문 시작
window.mainloop()
