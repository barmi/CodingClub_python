# circle.py
from turtle import *

# Draw a circle with radius of 50pixels. 반지름이 50픽셀인 원을 그립니다.
circle(50)

# Draw a semicircle with a radius 100pixels. 반지름이 100픽셀인 반원을 그립니다.
circle(100, extent=180)

# Draw a triangle which fits in a circle with a radius of 100pixels.
# 반경이 100픽셀인 삼각형을 그립니다.
circle(100, steps=3)

# Draw a pentagon which fits in a circle with a radius of 50pixels.
# 반경이 50픽셀인 오각형을 그립니다.
circle(50, steps=5)

# Tell Python to stop waiting for turtle instructions. turtle 명령어 입력이 끝났습니다.
done()
