# MyPong 메인 파일

from tkinter import *
import table, ball, bat

# 전역 변수 초기화
x_velocity = 10
y_velocity = 10

# tkinter 공장으로부터 윈도우 주문
window = Tk()
window.title("My Keepy Uppy Game")
       
# Table 공장으로부터 네트를 제외하고 table 주문
my_table = table.Table(window)

# Ball 공장으로부터 볼을 주문합니다
my_ball = ball.Ball(table=my_table, x_speed=x_velocity, y_speed=y_velocity,
                    width=24, height=24, colour="red", x_start=288, y_start=188)

# Bat 공장으로부터 왼쪽과 오른쪽 배트를 주문합니다
my_bat = bat.Bat(table=my_table, width=100, height=15, x_posn=250, y_posn=350, colour="blue")


#### 함수:
def game_flow():
    # 배트에서 공을 받아치는지 확인:
    my_bat.detect_collision(my_ball)
    
    my_ball.move_next()
    window.after(50, game_flow)

# 배트를 제어하기 위해 키보드의 키에 연결
window.bind("<Left>", my_bat.move_left)
window.bind("<Right>", my_bat.move_right)

# game_flow 반복문 호출
game_flow()

# tkinter 반복문 프로세스 시작
window.mainloop()
