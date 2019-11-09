import random
import turtle
import time
print("welcome to 007")
print("enter r to reload, s to shoot, and d to defend")
dead=False
global user_r
global comp_r
global user_action
global comp_action
user_r=0
comp_r=0
user_action="reload" or "shoot" or "defend"
comp_action="reload" or "shoot" or "defend"

def usrreload():
    global user_action
    global user_r
    user_action="reload"
    user_r+=1
        
def usrshoot():
    global user_action
    global user_r
    if user_r>0:
        user_r-=1
        user_action="shoot"
    else:
        print("you have 0 reloads left")
        user_action="reload"

def usrdefend():
    global user_action
    user_action="defend"
    

def cmpreload():
    global comp_action
    global comp_r
    comp_action="reload"
    comp_r+=1
    print("reload")

def cmpshoot():
    global comp_action
    global comp_r
    comp_action="shoot"
    if comp_r>0:
        comp_r-=1
        print("shoot")
    else:
        comp_action="defend"
        print("defend")

def cmpdefend():
    global comp_action
    comp_action="defend"
    print("defend")

def comp_play():
    if comp_r>=2:
        cmpshoot()
    else:
        sel=random.randint(1,3)
        if sel==1:
            cmpreload()
        elif sel==2:
            cmpshoot()
        elif sel==3:
            cmpdefend()
def user_play():
    user_input=input(":")
    if user_input=="s":
        usrshoot()
    elif user_input=="r":
        usrreload()
    elif user_input=="d":
        usrdefend()
    else:
        user_action="reload"
    
gamescreen=turtle.Screen()
gamescreen.bgcolor("black")
gamescreen.title("007")

comp=turtle.Turtle(shape="turtle")
comp.color("blue")
comp.ht()
comp.pu()
comp.speed(0)
comp.fd(200)
comp.seth(180)
comp.st()

user=turtle.Turtle(shape="turtle")
user.color("red")
user.ht()
user.pu()
user.speed(0)
user.bk(200)
user.st()

writer=turtle.Turtle()
writer.ht()
writer.pu()
writer.speed(0)
writer.color("orange")
writer.goto(-240,20)
writer.write("USER",font=("calibri",24))
writer.goto(150,20)
writer.write("COMP",font=("calibri",24))
writer.goto(-40,-50)

user_shield=turtle.Turtle(shape="square")
user_shield.ht()
user_shield.color("green")
user_shield.pu()
user_shield.bk(100)

comp_shield=turtle.Turtle(shape="square")
comp_shield.ht()
comp_shield.color("green")
comp_shield.pu()
comp_shield.fd(100)

bul=turtle.Turtle()
bul.ht()
bul.color("white")
bul.pu()
bul.speed(1)
bul.goto(-200,0)

bud=turtle.Turtle()
bud.ht()
bud.color("white")
bud.pu()
bud.speed(1)
bud.goto(200,0)
bud.seth(180)

while not dead:
    user_play()
    comp_play()
    if comp_action=="reload" and user_action=="shoot":
        bul.st()
        bul.fd(400)
        comp.ht()
        writer.write("YOU WIN",font=("calibri",24))
        dead=True
        print("you win")
    elif user_action=="reload" and comp_action=="shoot":
        bud.st()
        bud.fd(400)
        user.ht()
        writer.write("COMP WINS",font=("calibri",24))
        dead=True
        print("computer wins")
    elif user_action=="shoot" and comp_action=="shoot":
        bud.st()
        bul.st()
        for i in range(50):
            bul.fd(4)
            bud.fd(4)
        bul.ht()
        bud.ht()
        bul.bk(200)
        bud.bk(200)
    elif user_action=="shoot" and comp_action=="defend":
        comp_shield.st()
        bul.st()
        bul.fd(300)
        bul.ht()
        comp_shield.ht()
        bul.bk(300)
    elif user_action=="defend" and comp_action=="shoot":
        user_shield.st()
        bud.st()
        bud.fd(300)
        bud.ht()
        user_shield.ht()
        bud.bk(300)
    elif user_action=="defend" and comp_action=="defend":
        user_shield.st()
        comp_shield.st()
        time.sleep(1)
        user_shield.ht()
        comp_shield.ht()
    elif user_action=="reload" and comp_action=="defend":
        comp_shield.st()
        time.sleep(1)
        comp_shield.ht()
    elif comp_action=="reload" and user_action=="defend":
        user_shield.st()
        time.sleep(1)
        user_shield.ht()
turtle.mainloop()
















    
