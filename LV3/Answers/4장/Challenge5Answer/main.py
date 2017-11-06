# MyPong 메인 파일

from tkinter import *
import table, ball

# 전역 변수 초기화
x_velocity = 10
y_velocity = 10

# tkinter 공장으로부터 윈도우 주문
window = Tk()
window.title("MyPong")
       
# Table 공장으로부터 table 주문
my_table = table.Table(window, net_colour="green", vertical_net=True)

# Ball 공장으로부터 볼을 주문합니다
my_ball = ball.Ball(table=my_table, x_speed=x_velocity, y_speed=y_velocity,
                    width=24, height=24, colour="red", x_start=20, y_start=188)

#### 함수:
def game_flow():
    my_ball.move_next()
    window.after(50, game_flow)
    my_ball.y_speed = my_ball.y_speed + 10 # <--- 중력을 추가할 경우 여기에 씁니다

# game_flow 반복문 호출
game_flow()

# tkinter 반복문 프로세스 시작
window.mainloop()
