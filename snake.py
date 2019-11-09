import turtle
import random
import time

wn=turtle.Screen()
wn.bgcolor("blue")
wn.title("snake")
wn.setup(width=720 , height=720)
wn.tracer(0)

filler=turtle.Turtle()
filler.color("green")
filler.ht()
filler.goto(-310,310)
filler.begin_fill()
for i in range(4):
	filler.fd(620)
	filler.rt(90)
filler.end_fill()

head=turtle.Turtle()
head.pu()
head.shape("square")
head.direction= "none"

food=turtle.Turtle()
food.color("red")
food.pu()
food.shape("circle")
food.goto(0,60)

score= 0
highscore= 0

string="score : %s  highscore : %s" %(score , highscore)

sp=turtle.Turtle()
sp.ht()
sp.pu()
sp.color("white")
sp.goto(0,310)
sp.write(string,align="center",font=("arial",24))

def go_up():
	if head.direction!="down":
		head.direction="up"
def go_down():
	if head.direction!="up":
		head.direction="down"
def go_right():
	if head.direction!="left":
		head.direction="right"
def go_left():
	if head.direction!="right":
		head.direction="left"

segments=[]

turtle.listen()
wn.onkeypress(go_up , "w")		
wn.onkeypress(go_down , "s")
wn.onkeypress(go_right , "d")
wn.onkeypress(go_left , "a")

delay=0.1
while True:
	wn.update()
	time.sleep(delay)		
	
	lens = len(segments)
	
	if head.distance(food) < 20:
		x=random.randrange(-300,300,20)
		y=random.randrange(-300,300,20)
		food.goto(x,y)
		
		segment=turtle.Turtle()
		segment.pu()
		segment.color("grey")
		segment.shape("square")
		segments.append(segment)
		
		if delay > 0:
			delay-= 0.001
		
		score += 1
		if score>highscore:
			highscore=score
			
		string="score : %s  highscore : %s" %(score , highscore)
					
		sp.undo()
		sp.write(string,align="center",font=("arial",24))
		
	for i in range(lens-1,0,-1):
		sx=segments[i-1].xcor()
		sy=segments[i-1].ycor()
		segments[i].goto(sx,sy)
	
	if len(segments) > 0:
		hx=head.xcor()
		hy=head.ycor()
		segments[0].goto(hx,hy)
	
	
	if head.direction=="down":
		y=head.ycor()
		head.sety(y-20)
	if head.direction=="up":
		y=head.ycor()
		head.sety(y+20)
	if head.direction=="right":
		x=head.xcor()
		head.setx(x+20)
	if head.direction=="left":
		x=head.xcor()
		head.setx(x-20)
	
	
	box=head.xcor()
	boy=head.ycor()
	
	if box > 300 or box < -300 or boy > 300 or boy < -300:
		head.direction="none"
		head.goto(0,0)
		food.goto(0,60)
		for segment in segments:
			segment.ht()
		segments.clear()
		score=0
	for segment in segments:
		if segment.distance(head) < 20:
			head.direction="none"
			head.goto(0,0)
			food.goto(0,60)
			for segment in segments:
				segment.ht()
			segments.clear()			
			score=0
			
			
turtle.mainloop()
