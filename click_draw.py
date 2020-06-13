import turtle
from tkinter import *

wn=turtle.Screen()
wn.bgcolor("white")
wn.setup(width=800,height=800)
wn.tracer(0)

global size
size=20

a=turtle.Turtle()
a.shape("circle")
a.shapesize(1)
a.pensize(size)

save_tur=turtle.Turtle()
save_tur.color("green")
save_tur.pu()
save_tur.shape("square")
save_tur.goto(-375,370)
save_tur.write("save", font=("callibri",10))
save_tur.goto(-360,360)

load_tur=turtle.Turtle()
load_tur.color("blue")
load_tur.pu()
load_tur.shape("square")
load_tur.goto(-345,370)
load_tur.write("load", font=("callibri",10))
load_tur.goto(-330,360)

current_tool=turtle.Turtle()
current_tool.color("black")
current_tool.shape("square")
current_tool.seth(45)
current_tool.pu()
current_tool.goto(200,370)
current_tool.write("current tool",font=("callibri",20))
current_tool.goto(285,360)

selected_tool=turtle.Turtle()
selected_tool.color("grey")
selected_tool.seth(90)
selected_tool.pu()
selected_tool.goto(285,365)

size_writer=turtle.Turtle()
size_writer.pu()
size_writer.ht()
size_writer.goto(360,170)
size_writer.write(size,font=("callibri",15))

precise=turtle.Turtle()
precise.color("black")
precise.shape("square")
precise.seth(45)
precise.pu()
precise.goto(370,10)

precise_logo_1=turtle.Turtle()
precise_logo_1.color("grey")
precise_logo_1.pu()
precise_logo_1.seth(270)
precise_logo_1.goto(370,2)

precise_logo_2=turtle.Turtle()
precise_logo_2.color("grey")
precise_logo_2.pu()
precise_logo_2.shape("circle")
precise_logo_2.shapesize(0.5)
precise_logo_2.goto(370,12)

selected_color=turtle.Turtle()
selected_color.pu()
selected_color.shape("square")
selected_color.goto(-90,370)
selected_color.write("current color",font=("callibri",20))
selected_color.goto(0,360)
selected_color.color("red")

size_up=turtle.Turtle()
size_up.color("grey")
size_up.shape("square")
size_up.pu()
size_up.goto(370,160)

up_arrow=turtle.Turtle()
up_arrow.pu()
up_arrow.goto(370,165)
up_arrow.seth(90)

size_down=turtle.Turtle()
size_down.color("grey")
size_down.shape("square")
size_down.pu()
size_down.goto(370,138)

p_arrow=turtle.Turtle()
p_arrow.pu()
p_arrow.goto(370,133)
p_arrow.seth(270)

left_curve=turtle.Turtle()
left_curve.seth(45)
left_curve.shape("square")
left_curve.pu()
left_curve.color("black")
left_curve.goto(370,70)

left_arrow=turtle.Turtle()
left_arrow.color("grey")
left_arrow.pu()
left_arrow.goto(365,70)
left_arrow.seth(180)

right_curve=turtle.Turtle()
right_curve.seth(45)
right_curve.shape("square")
right_curve.pu()
right_curve.color("black")
right_curve.goto(370,40)

right_arrow=turtle.Turtle()
right_arrow.color("grey")
right_arrow.pu()
right_arrow.goto(375,40)
right_arrow.seth(0)

line_tool=turtle.Turtle()
line_tool.color("black")
line_tool.pu()
line_tool.shape("square")
line_tool.goto(370,100)
line_tool.seth(45)

line_up_arrow=turtle.Turtle()
line_up_arrow.color("grey")
line_up_arrow.pu()
line_up_arrow.goto(370,105)
line_up_arrow.seth(90)

margin_marker=turtle.Turtle()
margin_marker.color("black")
margin_marker.pu()
margin_marker.ht()
margin_marker.pensize(1)
margin_marker.goto(-400,340)
margin_marker.pd()
margin_marker.fd(750)
margin_marker.rt(90)
margin_marker.fd(680)

blue=turtle.Turtle()
blue.color("blue")
blue.shape("square")
blue.pu()
blue.goto(370,310)

red=turtle.Turtle()
red.color("red")
red.shape("square")
red.pu()
red.goto(370,280)

green=turtle.Turtle()
green.color("green")
green.shape("square")
green.pu()
green.goto(370,250)

yellow=turtle.Turtle()
yellow.color("yellow")
yellow.shape("square")
yellow.pu()
yellow.goto(370,220)
global select
select=False
global penc
penc="red"
global tool
tool="line"
global load_process
load_process="off"
pi=3.14159265358979323846264338327950288419716939937510
operations=[]
wn.update()
wn.tracer(1)

def save():
    global save_widget
    global master
    save_name=str(save_widget.get())+".ptf"
    ptfile=open(save_name,'w')
    for operation in operations:
        ptfile.write(operation+";")
    ptfile.close()
    master.destroy()
    
def mquit():
    global master
    master.destroy()

def load():
    global load_process
    global load_widget
    global master2
    global tool
    global select
    global penc
    global size
    load_process="on"
    load_name=str(load_widget.get())+".ptf"
    ptfile=open(load_name,'r')
    all_ops=ptfile.read()
    ptfile.close()
    master2.destroy()
    tool="line"
    select=False
    penc="red"
    selected_color.color(penc)
    size=20
    a.pensize(size)
    size_writer.undo()
    size_writer.write(size,font=("callibri",15))
    a.pu()
    a.goto(0,0)
    a.pd()
    wn.tracer(0)
    difs=all_ops.split(";")
    
    for xy in difs:
        if xy != "":
            x=float(xy.split(",")[0])
            y=float(xy.split(",")[1])
        main(x,y)
    wn.update()
    wn.tracer(1)
    select=False
    a.color("black")
    load_process="off"

def m2quit():
    global master2
    master2.destroy()

def m3quit():
    global master3
    master3.destroy()

def prec_draw():
    global xval
    global yval
    global master3
    x=float(xval.get())
    y=float(yval.get())
    master3.destroy()
    main(x,y)

def main(x,y):
    global xval
    global yval
    global master3
    global load_process
    global load_widget
    global master2
    global save_widget
    global master
    global penc
    global select
    global size
    global tool
    op=str(x)+","+str(y)
    #print(op)
    if save_tur.distance(x,y)<10:
        master=Tk()
        Label(master, text="Name the save file").grid(row=0)
        save_widget = Entry(master)
        save_widget.grid(row=0, column=1)
        Button(master, text="Cancel", command=mquit).grid(row=1, column=0, sticky='W'+'E')
        Button(master, text="Save", command=save).grid(row=1, column=1, sticky='W'+'E')
        master.mainloop()
    elif load_tur.distance(x,y)<10:
        master2=Tk()
        Label(master2, text="Name the File to load").grid(row=0)
        load_widget = Entry(master2)
        load_widget.grid(row=0,column=1)
        Button(master2, text="Cancel", command=m2quit).grid(row=1, column=0, sticky='W'+'E')
        Button(master2, text="Load", command=load).grid(row=1, column=1, sticky='W'+'E')
        master2.mainloop()
    elif precise.distance(x,y)<10:
        master3= Tk()
        Label(master3, text="current position: "+str(a.xcor())+" , "+str(a.ycor())).grid(row=3)
        Label(master3, text="x co-ordinate").grid(row=0)
        Label(master3, text="y co-ordinate").grid(row=1)
        xval= Entry(master3)
        yval= Entry(master3)
        xval.grid(row=0,column=1)
        yval.grid(row=1,column=1)
        Button(master3, text="Cancel", command=m3quit).grid(row=2, column=0, sticky="W"+"E")
        Button(master3, text="Draw", command=prec_draw).grid(row=2, column=1, sticky="W"+"E")
        master3.mainloop()
    else:
        operations.append(op)
        if blue.distance(x,y)<10:
            penc="blue"
            selected_color.color(penc)
        elif red.distance(x,y)<10:
            penc="red"
            selected_color.color(penc)
        elif green.distance(x,y)<10:
            penc="green"
            selected_color.color(penc)
        elif yellow.distance(x,y)<10:
            penc="yellow"
            selected_color.color(penc)
        elif line_tool.distance(x,y)<10:
            tool="line"
            selected_tool.goto(285,365)
            selected_tool.seth(90)
        elif right_curve.distance(x,y)<10:
            tool="right_curve"
            selected_tool.goto(290,360)
            selected_tool.seth(0)
        elif left_curve.distance(x,y)<10:
            tool="left_curve"
            selected_tool.goto(280,360)        
            selected_tool.seth(180)
        elif size_up.distance(x,y)<10:
            if size< 50:
                size+=1
                a.pensize(size)
                size_writer.undo()
                size_writer.write(size,font=("callibri",15))

        elif size_down.distance(x,y)<10:
            if size>1:
                size-=1
                a.pensize(size)
                size_writer.undo()
                size_writer.write(size,font=("callibri",15))
        
        

        elif not(x>325 or x<-400 or y>315 or y<-340):
            if tool=="line":
                if a.distance(x,y)>10:
                    if select:
                        a.goto(x,y)
                        select=False
                        a.color("black")
                    else:
                        a.pu()
                        a.goto(x,y)
                        a.pd()
                else:
                    if not select:
                        select=True
                        a.color(penc)
                    else:
                        select=False
                        a.color("black")
            elif tool=="right_curve":
                if a.distance(x,y)>10:
                    if select:
                        look=a.towards(x,y)
                        ac_ang=look+90
                        if (ac_ang)>360:
                            ac_ang-=360
                        a.seth(ac_ang)
                        diameter=a.distance(x,y)
                        circumference=diameter*pi
                        unit=(circumference/360)
                        wn.tracer(0)
                        for i in range(180):
                            a.fd(unit)
                            a.rt(1)
                            if load_process=="off":
                                wn.update()
                        if load_process=="off":
                            wn.tracer(1)
                        select=False
                        a.color("black")
                    else:
                        a.pu()
                        a.goto(x,y)
                        a.pd()
                else:
                    if select:
                        select=False
                        a.color("black")
                    else:
                        select=True
                        a.color(penc)
            elif tool=="left_curve":
                if a.distance(x,y)>10:
                    if select:
                        look=a.towards(x,y)
                        ac_ang=look-90
                        if (ac_ang)<0:
                            ac_ang+=360
                        a.seth(ac_ang)
                        diameter=a.distance(x,y)
                        circumference=diameter*pi
                        unit=(circumference/360)
                        wn.tracer(0)
                        for i in range(180):
                            a.fd(unit)
                            a.lt(1)
                            if load_process=="off":
                                wn.update()
                        if load_process=="off":
                            wn.tracer(1)
                        select=False
                        a.color("black")
                    else:
                        a.pu()
                        a.goto(x,y)
                        a.pd()
                else:
                    if select:
                        select=False
                        a.color("black")
                    else:
                        select=True
                        a.color(penc)
            
    
turtle.listen()
turtle.onscreenclick(main)
turtle.mainloop()
