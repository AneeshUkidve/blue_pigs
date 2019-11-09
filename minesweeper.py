#import modules
import turtle
import random

#declare global variable
global coul
coul=9
global row
row=9
global mines
mines=1

global first_click
first_click=True
global over
over=False

#set up the screen
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("MineSweeper")
wn.tracer(0)

print("blue   = 1")
print("\ngreen  = 2")
print("\nred    = 3")
print("\npurple = 4")
print("\nyellow = 5")
print("\nbrown  = 6")
print("\norange = 7")
print("\npink   = 8")

#list to access all the cells
minecells=[]

#class minecells
class minecell:
    def __init__(self,mine_id,has_mine,disc,shown):
        #mine_id is the number used to access the cell within the program
        #mine_id is unique i.e. no two cells have the same mine_id
        self.mid=mine_id
        #has_mine is a boolean that tells if there is a mine in the cell   
        self.exp=has_mine

        self.disc=disc
        #shown is a boolean which tells wether a given cel is shown or not
        self.shown=shown
        self.score=0
        self.flag=False
        
        minecells.append(self)#this enables us to access the cell from the list
        
        #the code from "if self.mid!=0:" till "self.man.goto(xpos,ypos)"
        #decides the position of the cell based on the number of rows and coulumns
        if self.mid!=0:
            xx=self.mid%coul
            if xx==0:
                xx=coul
            xpos=(xx*40)-((coul*20)+20)

            yy=row
            for i in range(row):
                if self.mid>(coul*(i+1)):
                    yy=row-(i+1)
            ypos=(yy*40)-((row*20)+20)
            
            self.man=turtle.Turtle()
            self.man.color("grey")
            self.man.pu()
            self.man.shape("square")
            self.man.shapesize(1.9)
            self.man.goto(xpos,ypos)

    def check_score(self):
        if self.mid!=0:
            if not self.exp:#if the cell is not a mine:
                score=0

                #check if the cell above is a mine
                top_id=int(self.mid - coul)
                if top_id > 0:
                    if minecells[top_id].exp:
                        score+=1

                # check if top right cell is a mine
                tr_id=int(self.mid-(coul-1))
                if tr_id > 0:
                    if tr_id%coul!=1:
                        if minecells[tr_id].exp:
                            score+=1

                #check if cell on right is a mine 
                r_id=int(self.mid + 1)
                if r_id%coul!=1:
                    if minecells[r_id].exp:
                        score+=1

                #check if bottom right cell is a mine
                br_id=int(self.mid + 1 + coul)
                if br_id <= (coul*row):
                    if br_id%coul!=1:
                        if minecells[br_id].exp:
                            score+=1

                #check if cell below is a mine
                b_id=int(self.mid + coul)
                if b_id <= (coul*row):
                    if minecells[b_id].exp:
                        score+=1

                #check if bottom left cell is a mine
                bl_id=int(self.mid + (coul-1))
                if bl_id < (coul*row):
                    if bl_id%coul!=0:
                        if minecells[bl_id].exp:
                            score+=1

                #check if cell on left is a mine
                l_id=int(self.mid - 1)
                if l_id%coul!=0:
                    if minecells[l_id].exp:
                        score+=1

                #check if top left cell is a mine
                tl_id=int(self.mid - (coul+1))
                if tl_id > 0:
                    if tl_id%coul!=0:
                        if minecells[tl_id].exp:
                            score+=1

                self.score=score

    def discovery(self):
        if self.mid!=0:
            if self.disc:
                if not self.shown:
                    if self.score==1:
                        self.man.color("blue")
                    elif self.score==2:
                        self.man.color("green")
                    elif self.score==3:
                        self.man.color("red")
                    elif self.score==4:
                        self.man.color("purple")
                    elif self.score==5:
                        self.man.color("yellow")
                    elif self.score==6:
                        self.man.color("brown")
                    elif self.score==7:
                        self.man.color("orange")
                    elif self.score==8:
                        self.man.color("pink")

                    self.shown=True
                    
    def zeero(self):
        if self.mid!=0:
            if not self.shown:
                self.man.color("white")
                self.shown=True
                top_id=int(self.mid - coul)
                if top_id > 0:
                    if minecells[top_id].score:
                        minecells[top_id].discovery()
                    else:
                        minecells[top_id].zeero()

                
                tr_id=int(self.mid-(coul-1))
                if tr_id > 0:
                    if tr_id%coul!=1:
                        if minecells[tr_id].score:
                            minecells[tr_id].discovery()
                        else:
                            minecells[tr_id].zeero()

            
                r_id=int(self.mid + 1)
                if r_id%coul!=1:
                    if minecells[r_id].score:
                        minecells[r_id].discovery()
                    else:
                        minecells[r_id].zeero()

                
                br_id=int(self.mid + 1 + coul)
                if br_id <= (coul*row):
                    if br_id%coul!=1:
                        if minecells[br_id].score:
                            minecells[br_id].discovery()
                        else:
                            minecells[br_id].zeero()

                
                b_id=int(self.mid + coul)
                if b_id <= (coul*row):
                    if minecells[b_id].score:
                        minecells[b_id].discovery()
                    else:
                        minecells[b_id].zeero()

                
                bl_id=int(self.mid + (coul-1))
                if bl_id < (coul*row):
                    if bl_id%coul!=0:
                        if minecells[bl_id].score:
                            minecells[bl_id].discovery()
                        else:
                            minecells[bl_id].zeero()

                
                l_id=int(self.mid - 1)
                if l_id%coul!=0:
                    if minecells[l_id].score:
                        minecells[l_id].discovery()
                    else:
                        minecells[l_id].zeero()

                
                tl_id=int(self.mid - (coul+1))
                if tl_id > 0:
                    if tl_id%coul!=0:
                        if minecells[tl_id].score:
                            minecells[tl_id].discovery()
                        else:
                            minecells[tl_id].zeero()

                
                    
def generate():
    for i in range((coul*row)+1):
        pix=minecell(i,False,True,False)

generate()
wn.update()

def main(x,y):
    global over
    global first_click
    global mines
    if not over:
        if first_click:
            for cel in minecells:
                if cel.mid:
                    if cel.man.distance(x,y) < 20:
                        first_click=False
                        
                        top_id=int(cel.mid - coul)
                        tr_id=int(cel.mid-(coul-1))
                        r_id=int(cel.mid + 1)
                        br_id=int(cel.mid + 1 + coul)
                        b_id=int(cel.mid + coul)
                        bl_id=int(cel.mid + (coul-1))
                        l_id=int(cel.mid - 1)
                        tl_id=int(cel.mid - (coul+1))
                        minelist=[]
                        while mines:
                            bore=0
                            mina=random.randint(1,(coul*row))
                            if mina!=top_id and mina!=tr_id and mina!=r_id and mina!=br_id and mina!=b_id and mina!=bl_id and mina!=l_id and mina!=tl_id and mina!=cel.mid:
                                for i in minelist:
                                    if mina==i:
                                        bore+=1
                                if not bore:
                                    minelist.append(mina)
                                    mines-=1
                                    minecells[mina].exp=True
                                    minecells[mina].shown=False

                        for bcv in minecells:
                            bcv.check_score()
                        
                        cel.zeero()
                        wn.update()
            
        else:
            for cel in minecells:
                if cel.mid:
                    if cel.man.distance(x,y) < 20:
                        if not cel.flag:
                            if cel.exp:
                                for c in minecells:
                                    if c.exp:
                                        a=turtle.Turtle()
                                        a.color("black")
                                        a.shape("turtle")
                                        a.shapesize(0.9)
                                        a.pu()
                                        a.goto(c.man.xcor(),c.man.ycor())
                                print("Game Over")
                                over=True
                            else:
                                if cel.score:
                                    cel.discovery()
                                else:
                                    cel.zeero()
                      
            wn.update()
            

    else:
        print("Game Over")


def flag(x,y):
    if not over:
        if not first_click:
            for cee in minecells:
                if cee.mid:
                    if cee.man.distance(x,y) < 20:
                        if not cee.shown:
                            if cee.flag:
                                cee.man.color("grey")
                                cee.man.shape("square")
                                cee.man.shapesize(1.9)
                                cee.flag=False
                            else:
                                cee.man.color("red")
                                cee.man.shape("triangle")
                                cee.man.shapesize(1.6)
                                cee.flag=True
    wn.update()                         

def wind(x,y):
    if not first_click:
        xttpr=0
        for bom in minecells:
            if bom.exp:
                if not bom.flag:
                    xttpr+=1
        
        if xttpr==0:
            print("\n\n\n\nYOU WIN !!!\n\n\n\n")
            over = True
        else:
            print("\n\n\n\nYOU LOSE !!!\n\n\n\n")
            for c in minecells:
                if c.exp:
                    a=turtle.Turtle()
                    a.color("black")
                    a.shape("turtle")
                    a.shapesize(0.9)
                    a.pu()
                    a.goto(c.man.xcor(),c.man.ycor())
            over=True
    wn.update()

turtle.listen()
turtle.onscreenclick(main, 1)
turtle.onscreenclick(wind, 2)
turtle.onscreenclick(flag, 3)

turtle.mainloop()





