#import modules
import turtle
import time

#setup the screen
wn=turtle.Screen()
wn.bgcolor("blue")
wn.title("conway's game of life")
wn.tracer(0)

global coul
coul=20
global row
row=20
global grid
grid=1
global sq_size
sq_size=0.9

all_cells=[]

class cell:
    def __init__(self, cell_id, condition_bool):
        self.isalive=condition_bool
        self.cell_id=cell_id
        self.temp=self.isalive
        all_cells.append(self)
        if self.cell_id!=0:
            xx=self.cell_id%coul
            if xx==0:
                xx=coul
            xpos=(xx*(20*grid))-((coul*(10*grid))+(10*grid))

            yy=row
            for i in range(row):
                if self.cell_id>(coul*(i+1)):
                    yy=row-(i+1)
            ypos=(yy*(20*grid))-((row*(10*grid))+(10*grid))
            
            self.man=turtle.Turtle()
            self.man.color("black")
            self.man.pu()
            self.man.shape("square")
            self.man.shapesize(sq_size)
            self.man.goto(xpos,ypos)
       
        
    
    def check_score(self):
        if self.cell_id!=0:
            if True:
                score=0
                #check if the cell above is a mine
                top_id=int(self. cell_id - coul)
                if top_id > 0:
                    if all_cells[top_id].isalive:
                        score+=1

                # check if top right cell is a mine
                tr_id=int(self. cell_id-(coul-1))
                if tr_id > 0:
                    if tr_id%coul!=1:
                        if all_cells[tr_id].isalive:
                            score+=1

                #check if cell on right is a mine 
                r_id=int(self. cell_id + 1)
                if r_id%coul!=1:
                    if all_cells[r_id].isalive:
                        score+=1

                #check if bottom right cell is a mine
                br_id=int(self. cell_id + 1 + coul)
                if br_id <= (coul*row):
                    if br_id%coul!=1:
                        if all_cells[br_id].isalive:
                            score+=1

                #check if cell below is a mine
                b_id=int(self. cell_id + coul)
                if b_id <= (coul*row):
                    if all_cells[b_id].isalive:
                        score+=1

                #check if bottom left cell is a mine
                bl_id=int(self. cell_id + (coul-1))
                if bl_id < (coul*row):
                    if bl_id%coul!=0:
                        if all_cells[bl_id].isalive:
                            score+=1

                #check if cell on left is a mine
                l_id=int(self. cell_id - 1)
                if l_id%coul!=0:
                    if all_cells[l_id].isalive:
                        score+=1

                #check if top left cell is a mine
                tl_id=int(self. cell_id - (coul+1))
                if tl_id > 0:
                    if tl_id%coul!=0:
                        if all_cells[tl_id].isalive:
                            score+=1
        
                self.score=score
                

    def state_change(self):
        if self.cell_id!=0:          
            if self.isalive:
                if self.score >= 4 or self.score <= 1:
                    self.temp=False
            else:
                if self.score==3:
                    self.temp=True
            
    def display_state_change(self):
        if self.cell_id!=0:            
            if self.temp:
                self.man.color("white")
            else:
                self.man.color("black")
    def change_actual_state(self):
        if self.cell_id!=0:        
            self.isalive=self.temp
        

glider=[(2*coul)-3,(3*coul)-3,(3*coul)-1,(4*coul)-3,(4*coul)-2]

                            
#creating all the cells        
def generate():
    for i in range((coul*row)+1):
        pix=cell(i,False)
generate()

def start(lis):
    for num in lis:
        all_cells[num].isalive=True
        all_cells[num].temp=True
        all_cells[num].man.color("white")

start(glider)

wn.update()

delay=0.1

def main(x,y):
    global sq_size
    h=0
    for gga in range((coul*row)+1):
        if gga!=0:
            if all_cells[gga].man.distance(x,y) < (sq_size*10):
                if all_cells[gga].isalive==False:
                    all_cells[gga].isalive=True
                    all_cells[gga].temp=True
                    all_cells[gga].man.color("white")
                    wn.update()
                else:
                    all_cells[gga].isalive=False
                    all_cells[gga].temp=False
                    all_cells[gga].man.color("black")
                    wn.update()

def bbGun():
    while True:
        for a_cell in all_cells:
            a_cell.check_score()
        for a_cell in all_cells:
            a_cell.state_change()
        for a_cell in all_cells:
            a_cell.display_state_change()
        for a_cell in all_cells:
            a_cell.change_actual_state()
        time.sleep(delay)
        wn.update()


turtle.listen()
turtle.onscreenclick(main)
wn.onkeypress(bbGun, "p")

turtle.mainloop()
