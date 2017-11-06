# MyPong 메인 파일

from tkinter import *
import table

# tkinter 윈도우 공장으로부터 윈도우를 주문합니다
window = Tk()
window.title("MyPong")
       
# Table 클래스로부터 table을 주문합니다
my_table = table.Table(window, net_colour="green", vertical_net=True)

# 애니메이션 반복을 시작합니다
window.mainloop()
