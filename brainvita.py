import turtle
import time

wn=turtle.Screen()
wn.bgcolor("grey")
wn.title("Brainvita")
wn.tracer(0)

draw=turtle.Turtle()
draw.pu()
draw.ht()
draw.color("blue")
draw.goto(-315,135)
draw.begin_fill()
for i in range(4):
    draw.fd(180)
    draw.lt(90)
    draw.fd(180)
    draw.rt(90)
    draw.fd(270)
    draw.rt(90)
draw.end_fill()
wn.update()

coul=7
row=7
choice=False
selected=101
select=False
blacklist=[]
marlist=[]

class blackey:
    def __init__(self,sid):
        self.sid=sid
        blacklist.append(self)
        if self.sid!=0:
            xx=self.sid%coul
            if xx==0:
                xx=coul
            xpos=(xx*90)-((coul*45)+45)

            yy=row
            for i in range(row):
                if self.sid>(coul*(i+1)):
                    yy=row-(i+1)
            ypos=(yy*90)-((row*45)+45)
            
            self.man=turtle.Turtle()
            if self.sid==1 or self.sid==2 or self.sid==8 or self.sid==9 or self.sid==6 or self.sid==7 or self.sid==13 or self.sid==14 or self.sid==36 or self.sid==37 or self.sid==41 or self.sid==42 or self.sid==43 or self.sid==44 or self.sid==48 or self.sid==49:
                self.man.color("grey")
            else:
                self.man.color("black")
            self.man.pu()
            self.man.shape("circle")
            self.man.shapesize(3.5)
            self.man.goto(xpos,ypos)

class marble:
    def __init__(self,marid,valid,state):
        self.mid=marid
        self.v=valid
        self.state=state
        if self.mid==1 or self.mid==2 or self.mid==8 or self.mid==9 or self.mid==6 or self.mid==7 or self.mid==13 or self.mid==14 or self.mid==36 or self.mid==37 or self.mid==41 or self.mid==42 or self.mid==43 or self.mid==44 or self.mid==48 or self.mid==49:
            self.v=False
            self.state=False
        marlist.append(self)
        if self.mid==25:
            self.state=False
        if self.v:
            xx=self.mid%coul
            if xx==0:
                xx=coul
            xpos=(xx*90)-((coul*45)+45)
            self.x=xpos

            yy=row
            for i in range(row):
                if self.mid>(coul*(i+1)):
                    yy=row-(i+1)
            ypos=(yy*90)-((row*45)+45)
            self.y=ypos

            self.man=turtle.Turtle()
            wn.colormode(255)
            self.man.pu()
            self.man.shapesize(3)
            self.man.shape("circle")
            self.man.color(39,99,45)
            self.man.goto(self.x,self.y)

def gen1():
    for i in range(49):
        asd=blackey(i+1)
def gen2():
    for i in range(49):
        das=marble(i+1,True,True)
gen1()
gen2()
marlist[24].man.ht()
wn.update()

def main(x,y):
    global select
    global selected
    sast=100
    choice=False
    for i in range(49):
        mab=marlist[i]
        if mab.v:
            if mab.man.distance(x,y)<35:
                sast=i
                choice=True
                break
    if choice:
        if select:
            if sast==selected:
                blacklist[sast].man.color(0,0,0)
                select=False
                selected=101

            else:
                if marlist[sast].state==False:
                    if sast>selected:
                        if (sast-14)==selected:
                            if marlist[sast-7].state:
                                vx=marlist[sast].x
                                vy=marlist[sast].y
                                gx=marlist[selected].x
                                gy=marlist[selected].y
                    
                                blacklist[selected].man.color(0,0,0)
                                wn.tracer(1)
                                marlist[selected].man.goto(vx,vy)
                                time.sleep(0.1)
                                marlist[sast-7].man.ht()
                                wn.tracer(0)
                                marlist[selected].man.goto(gx,gy)
                                marlist[selected].man.ht()
                                marlist[selected].state=False
                                marlist[sast-7].state=False
                                marlist[sast].state=True
                                marlist[sast].man.st()
                                select=False
                                
                        elif (sast-2)==selected and marlist[sast].y==marlist[selected].y:
                            if marlist[sast-1].state:
                                vx=marlist[sast].x
                                vy=marlist[sast].y
                                gx=marlist[selected].x
                                gy=marlist[selected].y                    
                                blacklist[selected].man.color(0,0,0)
                                wn.tracer(1)
                                marlist[selected].man.goto(vx,vy)
                                time.sleep(0.1)
                                marlist[sast-1].man.ht()
                                wn.tracer(0)
                                marlist[selected].man.goto(gx,gy)
                                marlist[selected].man.ht()
                                marlist[selected].state=False
                                marlist[sast-1].state=False
                                marlist[sast].state=True
                                marlist[sast].man.st()
                                select=False
                                
                    if sast<selected:
                        if (sast+14)==selected:
                            if marlist[sast+7].state:
                                vx=marlist[sast].x
                                vy=marlist[sast].y
                                gx=marlist[selected].x
                                gy=marlist[selected].y
                    
                                blacklist[selected].man.color(0,0,0)
                                wn.tracer(1)
                                marlist[selected].man.goto(vx,vy)
                                time.sleep(0.1)
                                marlist[sast+7].man.ht()
                                wn.tracer(0)
                                marlist[selected].man.goto(gx,gy)
                                marlist[selected].man.ht()
                                marlist[selected].state=False
                                marlist[sast+7].state=False
                                marlist[sast].state=True
                                marlist[sast].man.st()
                                select=False
                                
                        elif (sast+2)==selected and marlist[sast].y==marlist[selected].y:
                            if marlist[sast+1].state:
                                vx=marlist[sast].x
                                vy=marlist[sast].y
                                gx=marlist[selected].x
                                gy=marlist[selected].y
                    
                                blacklist[selected].man.color(0,0,0)
                                wn.tracer(1)
                                marlist[selected].man.goto(vx,vy)
                                time.sleep(0.1)
                                marlist[sast+1].man.ht()
                                wn.tracer(0)
                                marlist[selected].man.goto(gx,gy)
                                marlist[selected].man.ht()
                                marlist[selected].state=False
                                marlist[sast+1].state=False
                                marlist[sast].state=True
                                marlist[sast].man.st()
                                select=False
                                                
        else:
            if marlist[sast].state:
                selected=sast
                select=True
                blacklist[sast].man.color(255,0,0)        
    wn.update()

turtle.listen()
turtle.onscreenclick(main,1)
turtle.mainloop()

