import turtle as t
import random

t.shape("turtle")

t.up()
t.goto(-1000,500)
t.down()
t.goto(-1000,0)
t.goto(-500,0)
t.goto(-500,500)
t.goto(-1000,500) # 왼쪽 상단 500x500을 그림
t.up()
t.goto(-750,250) # 거북이를 사각형 가운데로 위치함

a=random.randint(0,45) # 0부터 45까지 a를 랜덤으로 추출
b=random.randint(85,95) # 85부터 95까지 b를 랜덤으로 추출
 
t.setheading(a) # 시작각도를 랜덤으로 추출

for x in range(1000000000000000000000000000): # 거의 무한대 반복
    while t.xcor() < -500: # 거북이가 오른쪽 벽에 닿을때까지 반복
        t.forward(1)   
    q=t.heading()
    t.setheading(b+q)
    while t.ycor() < 500: # 거북이가 위쪽 벽에 닿을때까지 반복
        t.forward(1)
    w=t.heading()
    t.setheading(b+w)
    while t.xcor() > -1000: # 거북이가 왼쪽 벽에 닿을때까지 반복
        t.forward(1)
    e=t.heading()    
    t.setheading(b+e)
    while t.ycor() > -0: # 거북이가 아래쪽 벽에 닿을때까지 반복
        t.forward(1)
    r=t.heading()    
    t.setheading(b+r)
    
