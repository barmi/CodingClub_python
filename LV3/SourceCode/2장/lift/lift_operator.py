# lift_operator.py

import lift

# lift 객체 생성
my_lift = lift.Lift()

# lift가 위치한 층 찾기
floor = my_lift.get_floor()
print("lift가 새로운 층으로 이동했습니다", floor)

# 새로운 층으로 lift 이동
my_lift.move_to_floor(5)

# 현재 lift가 위치한 층 찾기
floor = my_lift.get_floor()
print("lift가 새로운 층으로 이동했습니다", floor)
