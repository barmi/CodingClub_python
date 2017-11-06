# MyPong의 주된 파일을 만듭니다.

from tkinter import *
import table, ball

# 전역 변수 선언
x_velocity = 10
y_velocity = 10

# tkinter 공장으로부터 윈도우 주문
window = Tk()
window.title("MyPong")
       
# Table 공장으로부터 table 주문
my_table = table.Table(window, net_colour="green", vertical_net=True)

# Ball 공장으로부터 볼을 주문합니다
my_ball = ball.Ball(table=my_table, x_speed=x_velocity, y_speed=y_velocity,
                    width=24, height=24, colour="red", x_start=288, y_start=188)

#### 함수:
def game_flow():
    my_ball.move_next()
    window.after(50, game_flow)

# game_flow를 호출합니다.
game_flow()

# tkinter 반복문 프로세스를 시작합니다.
window.mainloop()
