import pygame
pygame.init()
import time
import random

scw=512
sch=512
wn=pygame.display.set_mode((scw,sch))
pygame.display.set_caption("Puzzle 15")


mother_cells=[]

class cell:
    def __init__(self,cell_id):
        self.n=cell_id
        self.piece=cell_id
        self.img=pygame.image.load(str(self.piece)+".png")

        ya=self.n//4
        self.y=(ya*128)

        xa=self.n%4
        self.x=(xa*128)

        wn.blit(self.img,(self.x , self.y))
        mother_cells.append(self)

    def refresh(self):
        self.img=pygame.image.load(str(self.piece)+".png")
        wn.blit(self.img,(self.x , self.y))
        

    
def right():
    for p in mother_cells:
        if p.piece==15:
            cel=p
    if cel.n%4 != 0:
        cel.piece = mother_cells[(cel.n-1)].piece
        mother_cells[(cel.n-1)].piece = 15

        mother_cells[(cel.n-1)].refresh()
        cel.refresh()

def left():
    for p in mother_cells:
        if p.piece==15:
            cel=p
    if cel.n%4 != 3:
        cel.piece = mother_cells[(cel.n+1)].piece
        mother_cells[(cel.n+1)].piece = 15

        mother_cells[(cel.n+1)].refresh()
        cel.refresh()

def down():
    for p in mother_cells:
        if p.piece==15:
            cel=p
    if cel.n >= 4:
        cel.piece = mother_cells[(cel.n-4)].piece
        mother_cells[(cel.n-4)].piece = 15

        mother_cells[(cel.n-4)].refresh()
        cel.refresh()

def up():
    for p in mother_cells:
        if p.piece==15:
            cel=p
    if cel.n <= 11:
        cel.piece = mother_cells[(cel.n+4)].piece
        mother_cells[(cel.n+4)].piece = 15

        mother_cells[(cel.n+4)].refresh()
        cel.refresh()

def scramble():
    for i in range(1000):
        a=random.randint(1,4)
        if a==1:
            up()
        elif a==2:
            right()
        elif a==3:
            down()
        elif a==4:
            left()

def generate():
    for i in range(16):
        sad=cell(i)
generate()
pygame.display.update()

ok=True
run=True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if ok:
            ok=False
            left()
            pygame.display.update()
            time.sleep(0.2)
            ok=True
    if keys[pygame.K_RIGHT]:
        if ok:
            ok=False
            right()
            pygame.display.update()
            time.sleep(0.2)
            ok=True
    if keys[pygame.K_UP]:
        if ok:
            ok=False
            up()
            pygame.display.update()
            time.sleep(0.2)
            ok=True
    if keys[pygame.K_DOWN]:
        if ok:
            ok=False
            down()
            pygame.display.update()
            time.sleep(0.2)
            ok=True
    if keys[pygame.K_SPACE]:
        if ok:
            ok=False
            scramble()
            pygame.display.update()
            time.sleep(1)
            ok=True

        
pygame.quit()








    
