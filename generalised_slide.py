#import modules
import turtle
import time



dig=input("Input:")

#set up the screen
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("key board")
wn.tracer(0)
time.sleep(5)
cells=[]

#data of the numbers
n0=[[0,0,0,0,0,0,0],[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1],[0,0,0,0,0,0,0]]
n1=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,1,1,1,1,1],[0,0,0,0,0,0,0]]
n2=[[0,0,0,0,0,0,0],[1,0,0,1,1,1,1],[1,0,0,1,0,0,1],[1,1,1,1,0,0,1],[0,0,0,0,0,0,0]]
n3=[[0,0,0,0,0,0,0],[1,0,0,1,0,0,1],[1,0,0,1,0,0,1],[1,1,1,1,1,1,1],[0,0,0,0,0,0,0]]
n4=[[0,0,0,0,0,0,0],[1,1,1,1,0,0,0],[0,0,0,1,0,0,0],[1,1,1,1,1,1,1],[0,0,0,0,0,0,0]]
n5=[[0,0,0,0,0,0,0],[1,1,1,1,0,0,1],[1,0,0,1,0,0,1],[1,0,0,1,1,1,1],[0,0,0,0,0,0,0]]
n6=[[0,0,0,0,0,0,0],[1,1,1,1,1,1,1],[1,0,0,1,0,0,1],[1,0,0,1,1,1,1],[0,0,0,0,0,0,0]]
n7=[[0,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,1,1,1,1,1,1],[0,0,0,0,0,0,0]]
n8=[[0,0,0,0,0,0,0],[1,1,1,1,1,1,1],[1,0,0,1,0,0,1],[1,1,1,1,1,1,1],[0,0,0,0,0,0,0]]
n9=[[0,0,0,0,0,0,0],[1,1,1,1,0,0,1],[1,0,0,1,0,0,1],[1,1,1,1,1,1,1],[0,0,0,0,0,0,0]]

space=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

la=[[0,1,1,1,1,1,1],[1,0,0,1,0,0,0],[1,0,0,1,0,0,0],[1,0,0,1,0,0,0],[0,1,1,1,1,1,1]]
lb=[[1,1,1,1,1,1,1],[1,0,0,1,0,0,1],[1,0,0,1,0,0,1],[1,0,0,1,0,0,1],[0,1,1,0,1,1,0]]
lc=[[0,1,1,1,1,1,0],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1]]
ld=[[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[0,1,1,1,1,1,0]]
le=[[1,1,1,1,1,1,1],[1,0,0,1,0,0,1],[1,0,0,1,0,0,1],[1,0,0,1,0,0,1],[1,0,0,0,0,0,1]]
lf=[[1,1,1,1,1,1,1],[1,0,0,1,0,0,0],[1,0,0,1,0,0,0],[1,0,0,1,0,0,0],[1,0,0,0,0,0,0]]
lg=[[0,1,1,1,1,1,0],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,1,0,1],[1,0,0,0,1,1,1]]
lh=[[1,1,1,1,1,1,1],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[1,1,1,1,1,1,1]]
li=[[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1]]
#lj=[[1,0,0,0,0,1,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0]]
lj=[[1,0,0,0,0,1,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1],[1,0,0,0,0,0,0]]
lk=[[1,1,1,1,1,1,1],[0,0,0,1,0,0,0],[0,0,1,0,1,0,0],[0,1,0,0,0,1,0],[1,0,0,0,0,0,1]]
ll=[[1,1,1,1,1,1,1],[0,0,0,0,0,0,1],[0,0,0,0,0,0,1],[0,0,0,0,0,0,1],[0,0,0,0,0,0,0]]
lm=[[1,1,1,1,1,1,1],[0,1,0,0,0,0,0],[0,0,1,1,0,0,0],[0,1,0,0,0,0,0],[1,1,1,1,1,1,1]]
ln=[[1,1,1,1,1,1,1],[0,1,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,1,0,0,0],[1,1,1,1,1,1,1]]
lo=[[0,1,1,1,1,1,0],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[0,1,1,1,1,1,0]]
lp=[[1,1,1,1,1,1,1],[1,0,0,1,0,0,0],[1,0,0,1,0,0,0],[1,0,0,1,0,0,0],[0,1,1,0,0,0,0]]
lq=[[0,1,1,1,1,1,0],[1,0,0,0,0,0,1],[1,0,0,0,1,0,1],[1,0,0,0,0,1,0],[0,1,1,1,1,0,1]]
lr=[[1,1,1,1,1,1,1],[1,0,0,1,0,0,0],[1,0,0,1,1,0,0],[1,0,0,1,0,1,0],[0,1,1,0,0,0,1]]
ls=[[0,1,1,0,0,1,0],[1,0,0,1,0,0,1],[1,0,0,1,0,0,1],[1,0,0,1,0,0,1],[0,1,0,0,1,1,0]]
lt=[[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,1,1,1,1,1,1],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0]]
lu=[[1,1,1,1,1,1,0],[0,0,0,0,0,0,1],[0,0,0,0,0,0,1],[0,0,0,0,0,0,1],[1,1,1,1,1,1,0]]
lv=[[1,1,1,0,0,0,0],[0,0,0,1,1,0,0],[0,0,0,0,0,1,1],[0,0,0,1,1,0,0],[1,1,1,0,0,0,0]]
lw=[[1,1,1,1,1,1,1],[0,0,0,0,0,1,0],[0,0,0,1,1,0,0],[0,0,0,0,0,1,0],[1,1,1,1,1,1,1]]
lx=[[1,1,0,0,0,1,1],[0,0,1,0,1,0,0],[0,0,0,1,0,0,0],[0,0,1,0,1,0,0],[1,1,0,0,0,1,1]]
ly=[[1,1,1,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,1,1,1],[0,0,0,1,0,0,0],[1,1,1,0,0,0,0]]
lz=[[1,0,0,0,0,1,1],[1,0,0,0,1,0,1],[1,0,0,1,0,0,1],[1,0,1,0,0,0,1],[1,1,0,0,0,0,1]]


#variables for later use
global current
current=0
global beu
beu=-1
global nex
nex=True
global dan
dan=0
global coul
coul=35
global row
row=7
global llen
llen=5

class pixcell:
    def __init__(self,pixcell_id,state):
        self.state=state
        self.temp=state
        self.pi_d=pixcell_id
        cells.append(self)
        
        if self.pi_d!=0:
            xx=self.pi_d%coul
            if xx==0:
                xx=coul
            xpos=(xx*20)-((coul*10)+10)

            yy=row
            for i in range(row):
                if self.pi_d>(coul*(i+1)):
                    yy=row-(i+1)
            ypos=(yy*20)-((row*10)+10)
            
            self.man=turtle.Turtle()
            self.man.color("grey")
            self.man.pu()
            self.man.shape("square")
            self.man.goto(xpos,ypos)

    def state_change(self):
        global current
        global nex
        global dan
        global coul
        global row
        
        if self.pi_d!=0:
            if self.pi_d%coul==0:
                if current==llen:
                    self.temp=False
                    nex=True
                else:
                    if dan[current][int((self.pi_d/coul)-1)]:
                        self.temp=True
                    else:
                        self.temp=False
            else:
                self.temp=cells[self.pi_d+1].state

    def actual(self):
        if self.pi_d!=0:
            self.state=self.temp

    def color(self):
        if self.pi_d!=0:
            if self.state:
                self.man.color("blue")
            else:
                self.man.color("grey")

def datar():
    global nex
    global beu
    global current
    global dan
    if nex:
        beu+=1
        if beu>=len(str(dig)):
            current=llen
        else:
            if (str(dig)[beu])=="0":
                dan=n0
            elif (str(dig)[beu])=="1":
                dan=n1
            elif (str(dig)[beu])=="2":
                dan=n2
            elif (str(dig)[beu])=="3":
                dan=n3
            elif (str(dig)[beu])=="4":
                dan=n4
            elif (str(dig)[beu])=="5":
                dan=n5
            elif (str(dig)[beu])=="6":
                dan=n6
            elif (str(dig)[beu])=="7":
                dan=n7
            elif (str(dig)[beu])=="8":
                dan=n8
            elif (str(dig)[beu])=="9":
                dan=n9

            elif str(dig)[beu]==" ":
                dan=space

            elif str(dig)[beu].upper()=="A":
                dan=la
            elif str(dig)[beu].upper()=="B":
                dan=lb
            elif str(dig)[beu].upper()=="C":
                dan=lc
            elif str(dig)[beu].upper()=="D":
                dan=ld
            elif str(dig)[beu].upper()=="E":
                dan=le
            elif str(dig)[beu].upper()=="F":
                dan=lf
            elif str(dig)[beu].upper()=="G":
                dan=lg
            elif str(dig)[beu].upper()=="H":
                dan=lh
            elif str(dig)[beu].upper()=="I":
                dan=li
            elif str(dig)[beu].upper()=="J":
                dan=lj
            elif str(dig)[beu].upper()=="K":
                dan=lk
            elif str(dig)[beu].upper()=="L":
                dan=ll
            elif str(dig)[beu].upper()=="M":
                dan=lm
            elif str(dig)[beu].upper()=="N":
                dan=ln
            elif str(dig)[beu].upper()=="O":
                dan=lo
            elif str(dig)[beu].upper()=="P":
                dan=lp
            elif str(dig)[beu].upper()=="Q":
                dan=lq
            elif str(dig)[beu].upper()=="R":
                dan=lr
            elif str(dig)[beu].upper()=="S":
                dan=ls
            elif str(dig)[beu].upper()=="T":
                dan=lt
            elif str(dig)[beu].upper()=="U":
                dan=lu
            elif str(dig)[beu].upper()=="V":
                dan=lv
            elif str(dig)[beu].upper()=="W":
                dan=lw
            elif str(dig)[beu].upper()=="X":
                dan=lx
            elif str(dig)[beu].upper()=="Y":
                dan=ly
            elif str(dig)[beu].upper()=="Z":
                dan=lz
            
            current=0
            
        nex=False        
    else:
        current+=1
        
            


def generate():
    for i in range((coul*row)+1):
        pix=pixcell(i,False)

generate()
wn.update()

while True:
    datar()
    
    for pixc in cells:
        pixc.state_change()

    for pixc in cells:
        pixc.actual()

    for pixc in cells:
        pixc.color()

    time.sleep(0.05)
    wn.update()
    
turtle.mainloop()
            
                
            
