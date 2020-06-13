import turtle
import time

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("OPPOSITION")
wn.tracer(0)

row=8
coul=8

legalist=[]
players=[]
colours=["blue", "red"]

class square:
    def __init__(self,sid):
        self.isLegal=True
        self.illegalPlayer=0
        self.sid=sid
        self.player=0
        legalist.append(self)
        if self.sid!=0:
            xx=self.sid%coul
            if xx==0:
                xx=coul
            xpos=(xx*40)-((coul*20)+20)

            yy=row
            for i in range(row):
                if self.sid>(coul*(i+1)):
                    yy=row-(i+1)
            ypos=(yy*40)-((row*20)+20)
            
            self.man=turtle.Turtle()
            self.man.color("white")
            self.man.pu()
            self.man.shape("square")
            self.man.shapesize(1.9)
            self.man.goto(xpos,ypos)

    def render(self):
        if self.isLegal:
            self.man.color("white")
            if self.player:
                players[self.player-1].man.goto(self.man.xcor(), self.man.ycor())


def locate(x):
    dayan=False
    for i in legalist:
        if i.sid==x:
            dayan=i
    return dayan

class player:
    def __init__(self, pid):
        self.pid=pid
        if self.pid==1:
            self.onSquare=1
            locate(1).player=1
        elif self.pid==2:
            self.onSquare=int((row*coul - coul)+1)
            locate(int((row*coul - coul)+1)).player=2
        self.man=turtle.Turtle()
        self.man.color(colours[self.pid-1])
        self.man.shape("circle")
        self.man.shapesize(1.1)
        self.man.pu()
        players.append(self)

    def neighbours(self):
        neighs=[]
        
        top_id=int(self.onSquare - coul)
        if top_id > 0:
            if locate(top_id):
                neighs.append(top_id)

        tr_id=int(self.onSquare-(coul-1))
        if tr_id > 0:
            if tr_id%coul!=1:
                if locate(tr_id):
                    neighs.append(tr_id)

        r_id=int(self.onSquare + 1)
        if r_id%coul!=1:
            if locate(r_id):
                neighs.append(r_id)

                
        br_id=int(self.onSquare + 1 + coul)
        if br_id <= (coul*row):
            if br_id%coul!=1:
                if locate(br_id):
                    neighs.append(br_id)

                
        b_id=int(self.onSquare + coul)
        if b_id <= (coul*row):
            if locate(b_id):
                neighs.append(b_id)
        
        
        bl_id=int(self.onSquare + (coul-1))
        if bl_id < (coul*row):
            if bl_id%coul!=0:
                if locate(bl_id):
                    neighs.append(bl_id)

        l_id=int(self.onSquare - 1)
        if l_id%coul!=0:
            if locate(l_id):
                neighs.append(l_id)


        tl_id=int(self.onSquare - (coul+1))
        if tl_id > 0:
            if tl_id%coul!=0:
                if locate(tl_id):
                    neighs.append(tl_id)
                
        return neighs

    def move(self, place):
        capture=False
        for ib in players:
            if ib.onSquare==place:
                jadu=ib
                capture=True
            
        if capture:    
            print("Game end\n", colours[self.pid-1], "wins")
            for l in legalist:
                legalist.remove(l)
        else:
            oldsq=self.onSquare
            locate(place).player=self.pid
            self.onSquare=place
            locate(oldsq).illegalPlayer=self.pid        
            locate(oldsq).man.color(colours[locate(oldsq).illegalPlayer - 1])
            legalist.remove(locate(oldsq))
        

def sqGen():
    for i in range(row*coul):
        alabama=square(i+1)
    wn.update()

def plGen():
    for i in range(2):
        alabam=player(i+1)

sqGen()
plGen()

for i in legalist:
    i.render()
wn.update()


turn=1

def main(x,y):
    global turn
    if turn%2==1:
        played=0
    else:
        played=1
    junaid=False
    for i in legalist:
        if i.man.distance(x,y) < 19:
            junaid=i
    if junaid:
        neigh=players[played].neighbours()
        if neigh==[]:
            print("Game end\n", colours[players[played].pid-1], "loses")
            for l in legalist:
                legalist.remove(l)
        else:
            valid=False
            for v in neigh:
                if int(v)==int(junaid.sid):
                    valid=True
            if valid:
                players[played].move(junaid.sid)
                for c in legalist:
                    c.render()
                wn.update()
                turn+=1



turtle.listen()
turtle.onscreenclick(main, 1)


turtle.mainloop()

        
            







