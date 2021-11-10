import pygame
import random
from covidgame import *
pygame.init()
ngang = 720
doc = 720
sc = pygame.display.set_mode((ngang,doc))
pygame.display.set_caption("Covid Game")
diem = 0
image = []
for i in range(0,48):
    image.append("covid/cv" + str(i) + ".png")
corona = actor(image)
corona.changesize(0.5)
corona.setlimit(0,720,0,620)
goc = 0
khoangtre = 0
def coronamove():
    global goc, khoangtre
    if khoangtre == 0:
        goc = random.randint(0,359)
        khoangtre = 600
    khoangtre = khoangtre - 1
    corona.move(270,0.5)

image = []
for i in range(0,33):
    image.append("spaceship/sp-" + str(i) + ".png")
spaceship = actor(image)
spaceship.changesize(0.3)
spaceship.setlimit(0,720,620,720)
spaceship.y = (620 + 720) /2
moveleft = moveright = False
def spaceshipmove():
    if moveright == True:
        spaceship.move(0,0.5)
    if moveleft == True:
        spaceship.move(180,0.5)

image = []
for i in range(0,82):
    image.append("laser/ls-" + str(i) + ".png")
laser = actor(image)
laser.changesize(0.3)
laserkhoangtre = 0
def lasermove():
    global laserkhoangtre
    if laserkhoangtre == 0:
        laserkhoangtre = 1440
        laser.x = spaceship.x
        laser.y = spaceship.y
    laserkhoangtre = laserkhoangtre - 1
    laser.move(90,0.5)

def hitcorona():
    global laserkhoangtre, diem, run
    if hitbox(laser,corona):
        corona.x = random.randint(0,720)
        corona.y = random.randint(0,500)
        laser.x = spaceship.x
        laser.y = spaceship.y
        laserkhoangtre = 1440
        diem = diem + 1
    if corona.y > 570:
        run = False
        pygame.quit()

def draw():
    sc.fill((0,0,0))
    corona.draw(sc)
    spaceship.draw(sc)
    laser.draw(sc)
    text(sc,str(diem),0,0,80,30,textsize = 20)
    pygame.draw.rect(sc,(255,0,0),(0,610,720,10))
    pygame.display.update()

def event():
    global run, moveright, moveleft
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
            pygame.quit()
        if e.type == pygame.KEYDOWN:
            if (e.key == pygame.K_RIGHT):
                moveright = True
            if (e.key == pygame.K_LEFT):
                moveleft = True
        if e.type == pygame.KEYUP:
            if (e.key == pygame.K_RIGHT):
                moveright = False
            if (e.key == pygame.K_LEFT):
                moveleft = False

run = True
while run:
    draw()
    event()
    coronamove()
    spaceshipmove()
    lasermove()
    hitcorona()
