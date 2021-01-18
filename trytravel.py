#interstellar
import pgzrun
from random import randint
import random
from pygame import mixer  #module for playing music  
mixer.init()  #initializing the module mixer
mixer.music.load('C:\\Users\\pc\code\interstellar\music\walker.mp3')
#loading the music i edited the countdown voice and song and made it one 
mixer.music.play() #playing it

score=0      
HEIGHT = 500
WIDTH  =700

rocket= Actor("rocket")
rocket.bottom =HEIGHT 
rocket.x = WIDTH//2

soil=Actor("soil")
soil.bottom=630
soil.x=0

astroids = []
meteroids =[]
clouds =[]
is_rocket_dead =False

def draw():
    screen.clear()
    level()
    rocket.draw()
    screen.draw.text("score :"+str(score),(10,0),fontsize =40,fontname="courbd_0",color="white")
    for astroid in astroids:
        astroid.draw()
    for meteroid in meteroids:
        meteroid.draw()
    if score<750:
        for cloud in clouds:
            cloud.draw()
    if score<10:
        soil.draw()
    
def update():
    move_rocket()
    move_astroid()
    move_meteroid()
    move_cloud()
    rocket_collision()

def move_astroid():
    for astroid in astroids:
        if astroid.top > HEIGHT:
            astroids.remove(astroid)
            create_astroid()
        else:
            astroid.y += 5
            astroid.angle+=-5

def move_cloud():
    for cloud in clouds:
        if cloud.top > HEIGHT:
            clouds.remove(cloud)
            create_cloud()
        else:
            cloud.y += 5
            
            

def move_meteroid():
    for meteroid in meteroids:
        if meteroid.right> WIDTH:
            meteroids.remove(meteroid)
            create_meteroid()
        else:
            meteroid.x += 5
            meteroid.angle+=+5
        

def create_astroid():
    astroid=Actor("meteorgrey1")
    astroid.top =0
    astroid.x=randint(50,WIDTH-50)
    astroids.append(astroid)

def create_meteroid():
    meteroid=Actor("meteorbrownbig1")
    meteroid.x=0
    meteroid.y=randint(50,HEIGHT-50)
    meteroids.append(meteroid)

def create_cloud():
    cloud=Actor("cloud3")
    cloud.y=0
    cloud.x=randint(50,WIDTH-50)
    clouds.append(cloud)
    
def move_rocket():
    if keyboard.left:
        rocket.x-=10
    elif keyboard.right:
        rocket.x+=10
    elif keyboard.up:
        rocket.y-=10
    elif keyboard.down:
        rocket.y+=10
    elif(keyboard.a):
        rocket.y-=1
        rocket.angle+=1
    elif (keyboard.d):
        rocket.y-=1
        rocket.angle-=1

    

def rocket_collision():
    global score,meteroid,astroid,roid
    for astroid in astroids:
        if astroid.colliderect(rocket):
            rocket.image="damageship"
            astroids.remove(astroid)
            meteroids.remove(meteroid)
            is_rocket_dead = True
        else:
            score+=1
    for meteroid in meteroids:
        if meteroid.colliderect(rocket):
            rocket.image="damageship"
            meteroids.remove(meteroid)
            astroids.remove(astroid)
            is_rocket_dead = True
        else:
            score+=1
    if score<750:        
        for cloud in clouds :
            score+=1
    
            
def level():
    global score
    if score >750:
        Z=(0,0,0)
        screen.fill(Z)
    else:
        x=(53,81,93)
        screen.fill(x)

def liftof():
    animate(rocket, tween='linear',pos=(350,250))
    #animating the initial launch 

def slow_down():
    animate(rocket,tween='linear',pos=(350,450))

   
#used this clss  clock  to shedule the astroids and clouds 
clock.schedule(create_astroid, 20.0)
clock.schedule(create_meteroid, 20.0)
clock.schedule(create_cloud, 8.0)
clock.schedule(liftof, 8.0)
clock.schedule(slow_down,18.0)

pgzrun.go()
