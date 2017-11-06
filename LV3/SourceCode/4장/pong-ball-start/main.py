# MyPong의 주된 파일을 만듭니다.

from tkinter import *
import table   #### <--- import ball 하는 것을 잊지마세요. ####

# 전역 변수 선언


# tkinter 공장으로부터 윈도우 주문
window = Tk()
window.title("MyPong")
       
# Table 공장으로부터 table 주문
my_table = table.Table(window, net_colour="green", vertical_net=True)

# Ball 공장으로부터 볼을 주문합니다

#### 함수:

# game_flow를 호출합니다.


# tkinter 반복문 프로세스를 시작합니다.
window.mainloop()
