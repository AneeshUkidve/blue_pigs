import turtle
import tkinter

make=turtle.Screen()
make.bgcolor("white")
make.tracer(0)

row=12
coul=7

a=turtle.Turtle()
a.ht()
a.pu()
a.goto(-200, 200)
a.color("black")
a.shapesize(10)
a.write("Middle Mouse button to save", font=("arial", 25))
a.goto(-582,0)
a.write("Left Mouse button for walls", font=("arial", 25))
a.goto(200,0)
a.write("Right Mouse button for start pos", font=("arial", 25))

cellist=[]

class adcell:
    def __init__(self,adid):
        self.state=0
        self.adid=adid
        cellist.append(self)
        if self.adid!=0:
            xx=self.adid%coul
            if xx==0:
                xx=coul
            xpos=(xx*40)-((coul*20)+20)

            yy=row
            for i in range(row):
                if self.adid>(coul*(i+1)):
                    yy=row-(i+1)
            ypos=(yy*40)-((row*20)+20)
            
            self.man=turtle.Turtle()
            self.man.color("grey")
            self.man.pu()
            self.man.shape("square")
            self.man.shapesize(1.9)
            self.man.goto(xpos,ypos)

for i in range(row*coul):
    adcell(i+1)
cellist[0].man.color("red")
cellist[0].state=2
make.update()

def wne(x,y):
    for cel in cellist:
        if cel.man.distance(x,y) < (19):
            if cel.state==0:
                cel.state=1
                cel.man.color("white")
                make.update()
            elif cel.state==1:
                cel.state=0
                cel.man.color("grey")
                make.update()

def starter(x,y):
    for cel in cellist:
        if cel.state==2:
            go=cel.adid
    for cel in cellist:
        if cel.man.distance(x,y) < (19):
            cellist[go-1].state=0
            cellist[go-1].man.color("grey")
            cel.state=2
            cel.man.color("red")
            make.update()

def save(x,y):
    answer=tkinter.simpledialog.askstring("SAVE", "Enter Level Name")
    lvlstr=""
    for ceel in cellist:
        if ceel.state==2:
            lvlstr=lvlstr+str(ceel.adid)
    for ceel in cellist:
        if ceel.state==1:
            lvlstr=lvlstr+"_"+str(ceel.adid)
    lvlstr=answer+"_"+lvlstr
    f=open("levels.txt", "a")
    f.write("\n"+lvlstr)
    f.close()
        

turtle.listen()
        
turtle.onscreenclick(wne, 1)
turtle.onscreenclick(starter, 3)
turtle.onscreenclick(save, 2)

turtle.mainloop()





























