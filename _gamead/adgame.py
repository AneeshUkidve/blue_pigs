import turtle
import tkinter

wn=turtle.Screen()
wn.bgcolor("white")
wn.tracer(0)

row=12
coul=7

glist=[]

a=turtle.Turtle()
a.ht()
a.pu()
a.goto(-320, 200)
a.color("black")
a.shapesize(10)
a.write("OnLy 1% oF PeOpLe CaN soLvE tHiS LeVeL", font=("times new roman", 25))


class gcell:
    def __init__(self,gid):
        self.state=0
        self.gid=gid
        self.ismark=False
        glist.append(self)
        if self.gid!=0:
            xx=self.gid%coul
            if xx==0:
                xx=coul
            xpos=(xx*40)-((coul*20)+20)

            yy=row
            for i in range(row):
                if self.gid>(coul*(i+1)):
                    yy=row-(i+1)
            ypos=(yy*40)-((row*20)+20)
            
            self.man=turtle.Turtle()
            self.man.color("grey")
            self.man.pu()
            self.man.shape("square")
            self.man.shapesize(1.9)
            self.man.goto(xpos,ypos)

for i in range(row*coul):
    gcell(i+1)

ball=turtle.Turtle()
ball.color("red")
ball.shape("circle")
ball.shapesize(1.5)
ball.pu()

def initiate(x,y):
    levname=tkinter.simpledialog.askstring("LOAD", "Enter Level Name")
    f=open("levels.txt", "r")
    levels=f.readlines()
    f.close()
    lvl=[1,1]
    for i in levels:
        if i.split("_")[0]==(levname):
            lvl=i.split("_")
    del(lvl[0])
    for  egs in glist:
        egs.state=0
        egs.ismark=False
        egs.man.color("grey")
    glist[int(lvl[0])-1].ismark=True
    glist[int(lvl[0])-1].man.color("green")
    ball.goto(glist[int(lvl[0])-1].man.xcor(), glist[int(lvl[0])-1].man.ycor())
    del(lvl[0])
    for wall in lvl:
        glist[int(wall)-1].state=1
        glist[int(wall)-1].man.color("white")

    wn.update()
    turtle.listen()
def go_up():
    for i in glist:
        if i.ismark:
            bell=i
    psy=(bell.gid-coul)
    if psy>0:
        psy=glist[psy-1]
        if psy.state==0:
            bell.ismark=False
            psy.ismark=True
            wn.tracer(2)
            psy.man.color("green")
            ball.goto(psy.man.xcor(),psy.man.ycor())
            wn.tracer(0)
            go_up()

def go_down():
    for i in glist:
        if i.ismark:
            bell=i
    psy=(bell.gid+coul)
    if psy<=coul*row:
        psy=glist[psy-1]
        if psy.state==0:
            bell.ismark=False
            psy.ismark=True
            wn.tracer(2)
            psy.man.color("green")
            ball.goto(psy.man.xcor(),psy.man.ycor())
            wn.tracer(0)
            go_down()

def go_right():
    for i in glist:
        if i.ismark:
            bell=i
    psy=(bell.gid+1)
    if psy<=coul*row and psy%coul!=1:
        psy=glist[psy-1]
        if psy.state==0:
            bell.ismark=False
            psy.ismark=True
            wn.tracer(2)
            psy.man.color("green")
            ball.goto(psy.man.xcor(),psy.man.ycor())
            wn.tracer(0)
            go_right()

def go_left():
    for i in glist:
        if i.ismark:
            bell=i
    psy=(bell.gid-1)
    if psy>0 and psy%coul!=0:
        psy=glist[psy-1]
        if psy.state==0:
            bell.ismark=False
            psy.ismark=True
            wn.tracer(2)
            psy.man.color("green")
            ball.goto(psy.man.xcor(),psy.man.ycor())
            wn.tracer(0)
            go_left()


turtle.onscreenclick(initiate, 2)
turtle.listen()
wn.onkeypress(go_up , "Up")		
wn.onkeypress(go_down , "Down")
wn.onkeypress(go_right , "Right")
wn.onkeypress(go_left , "Left")
            
turtle.mainloop()





























    
