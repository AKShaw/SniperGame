#image paths
level1 = "images\\level1.jpg"
mouseimage = "images\\scope.png"
bulletimg = "images\\ammo_full.png"
enemyimg = "images\\placeholder.png"
muzzleFlashIMG = "images\\muzzleFlash.png"

#blood
b1i = "images\\red\\1.png"
b2i = "images\\red\\2.png"
b3i = "images\\red\\3.png"
b4i = "images\\red\\4.png"
b5i = "images\\red\\5.png"
b6i = "images\\red\\6.png"
b7i = "images\\red\\7.png"
b8i = "images\\red\\8.png"
b9i = "images\\red\\9.png"
b10i = "images\\red\\10.png"

#sound paths
shotSF = "sounds\\shot.wav"
enemyShotSF = "sounds\\enemyShot.wav"

#imports
import pygame, sys, time, math, pygame.mixer, random
from pygame.locals import *

#sound vars
pygame.mixer.init()
shot = pygame.mixer.Sound(shotSF)
enemyShot = pygame.mixer.Sound(enemyShotSF)

#game vars
health  = 100
score = 0
ammo = 10
level = 1
level1EnemyPosX = [30,275,435,693,837,1011,1218]
level1EnemyPosY = [308,92,256,292,397,21,193]
enemysLeft = 7
ammoCheck = True
healthCheck = True
canFire = True

#screen setup
pygame.init()
screen = pygame.display.set_mode((1280,720),0,32)
pygame.display.set_caption("Stick Sniper v0.1! Level 1")

#convert images + set mouse visible to false
background = pygame.image.load(level1).convert()
mouseC = pygame.image.load(mouseimage).convert_alpha()
bullet = pygame.image.load(bulletimg).convert_alpha()
enemy = pygame.image.load(enemyimg).convert_alpha()
muzzleFlash = pygame.image.load(muzzleFlashIMG).convert_alpha()
pygame.mouse.set_visible(False)

#convert blood
b1 = pygame.image.load(b1i).convert_alpha()
b2 = pygame.image.load(b2i).convert_alpha()
b3 = pygame.image.load(b3i).convert_alpha()
b4 = pygame.image.load(b4i).convert_alpha()
b5 = pygame.image.load(b5i).convert_alpha()
b6 = pygame.image.load(b6i).convert_alpha()
b7 = pygame.image.load(b7i).convert_alpha()
b8 = pygame.image.load(b8i).convert_alpha()
b9 = pygame.image.load(b9i).convert_alpha()
b10 = pygame.image.load(b10i).convert_alpha()

while True:
    #mouse coords
    x,y = pygame.mouse.get_pos()
    x -= mouseC.get_width()/2
    y -= mouseC.get_height()/2
    
    for event in pygame.event.get():
        #Key press events
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_s:
                score = score + 10
            elif event.key == K_h:
                health = health - 10
        #shot handler
        if event.type == MOUSEBUTTONDOWN and event.button == 1 and canFire == True:
            x,y = pygame.mouse.get_pos()
            #Checks if the enemy is at mouse x and mouse y, moves them.
            if x>level1EnemyPosX[0] and x<level1EnemyPosX[0]+16 and y>level1EnemyPosY[0] and y<level1EnemyPosY[0]+16:
                score = score + 10
                level1EnemyPosX[0],level1EnemyPosY[0] = -16,-16
                enemysLeft = enemysLeft - 1
            elif x>level1EnemyPosX[1] and x<level1EnemyPosX[1]+16 and y>level1EnemyPosY[1] and y<level1EnemyPosY[1]+16:
                score = score + 10
                level1EnemyPosX[1],level1EnemyPosY[1] = -16,-16
                enemysLeft = enemysLeft - 1
            elif x>level1EnemyPosX[2] and x<level1EnemyPosX[2]+16 and y>level1EnemyPosY[2] and y<level1EnemyPosY[2]+16:
                score = score + 10
                level1EnemyPosX[2],level1EnemyPosY[2] = -16,-16
                enemysLeft = enemysLeft - 1
            elif x>level1EnemyPosX[3] and x<level1EnemyPosX[3]+16 and y>level1EnemyPosY[3] and y<level1EnemyPosY[3]+16:
                score = score + 10
                level1EnemyPosX[3],level1EnemyPosY[3] = -16,-16
                enemysLeft = enemysLeft - 1
            elif x>level1EnemyPosX[4] and x<level1EnemyPosX[4]+16 and y>level1EnemyPosY[4] and y<level1EnemyPosY[4]+16:
                score = score + 10
                level1EnemyPosX[4],level1EnemyPosY[4] = -16,-16
                enemysLeft = enemysLeft - 1
            elif x>level1EnemyPosX[5] and x<level1EnemyPosX[5]+16 and y>level1EnemyPosY[5] and y<level1EnemyPosY[5]+16:
                score = score + 10
                level1EnemyPosX[5],level1EnemyPosY[5] = -16,-16
                enemysLeft = enemysLeft - 1
            elif x>level1EnemyPosX[6] and x<level1EnemyPosX[6]+16 and y>level1EnemyPosY[6] and y<level1EnemyPosY[6]+16:
                score = score + 10
                level1EnemyPosX[6],level1EnemyPosY[6] = -16,-16
                enemysLeft = enemysLeft - 1
            #misc shot stuff
            ammo = ammo - 1
            shot.play()
            x -=muzzleFlash.get_width()/2
            y -= muzzleFlash.get_height()/2
            screen.blit(muzzleFlash, (x,y))
            pygame.display.update()
            time.sleep(0.125)
            pygame.display.update()
            time.sleep(0.125)
    #next level

    #if event.type == MOUSEBUTTONDOWN and event.button == 1 and canFire == False:
    #    x,y = pygame.mouse.get_pos()
    #    if x>(1280/2-(labelLevelDone.get_width()/2) and x<(1280/2-(labelLevelDone.get_width()/2+labelLevelDone.get_width()) and y>(720/2-(labelLevelDone.get_height()/2) and y<(720/2-(labelLevelDone.get_height()/2+labelLevelDone.get_height()):
    #        python ('level2.py')
    #        sys.exit()
    #        pygame.quit()   if x>(1280/2-(labelLevelDone.get_width()/2) and x<(1280/2-(labelLevelDone.get_width()/2+labelLevelDone.get_width()) and y>(720/2-(labelLevelDone.get_height()/2) and y<(720/2-(labelLevelDone.get_height()/2+labelLevelDone.get_height()):
    #        python ('level2.py')
    #        sys.exit()
    #        pygame.quit()

    #Enemy shot handler
    if enemysLeft != 0:
        MaxRandNum = math.floor(1000/enemysLeft)
    RandNum = random.randint(1,MaxRandNum)
    if RandNum == enemysLeft:
        health = health - 10
        enemyShot.play()

    #display vars
    font = pygame.font.SysFont("Ariel", 72)
    labelScore = font.render("Score : " + str(score), 1, (184,184,184))
    labelHealth = font.render("Health : " + str(health), 1, (184,184,184))
    labelAmmo = font.render(str(ammo), 1, (184,184,184))
    labelGameOverHealth = font.render("You died! Game over :(", 1, (184,184,184))
    labelGameOverAmmo = font.render("You ran out of ammo ! Game over :(", 1, (184,184,184))
    labelLevelDone = font.render("Level complete! click here for the next level.", 1, (184,184,184))

    #put bg on screen
    screen.blit(background, (0,0))
    screen.blit(mouseC, (x,y))
    screen.blit(labelScore, (1280-labelScore.get_width()-5,5))
    screen.blit(labelHealth, (5,5))
    screen.blit(bullet, (1280/2-bullet.get_width()/2-3,5+labelAmmo.get_height()/2-bullet.get_height()/2))
    screen.blit(labelAmmo, (1280/2+labelAmmo.get_width()+3/2,5))
    
    #checks
    #health
    if health <= 0 and healthCheck == True:
        screen.blit(labelGameOverHealth, (1280/2-(labelGameOverHealth.get_width()/2),720/2-(labelGameOverHealth.get_height()/2)))
        pygame.display.update()
        sys.exit()
        pygame.quit()
    
    #draw enemys
    screen.blit(enemy, (level1EnemyPosX[0],level1EnemyPosY[0]))
    screen.blit(enemy, (level1EnemyPosX[1],level1EnemyPosY[1]))
    screen.blit(enemy, (level1EnemyPosX[2],level1EnemyPosY[2]))
    screen.blit(enemy, (level1EnemyPosX[3],level1EnemyPosY[3]))
    screen.blit(enemy, (level1EnemyPosX[4],level1EnemyPosY[4]))
    screen.blit(enemy, (level1EnemyPosX[5],level1EnemyPosY[5]))
    screen.blit(enemy, (level1EnemyPosX[6],level1EnemyPosY[6]))

    #ammo
    if ammo <= 0 and ammoCheck == True:
        screen.blit(labelGameOverAmmo, (1280/2-(labelGameOverAmmo.get_width()/2),720/2-(labelGameOverAmmo.get_height()/2)))
        pygame.display.update()
        sys.exit()
        pygame.quit()

    #add health to score and shows button
    if score >= 70:
        score = score + health
        healthCheck = False
        ammoCheck = False
        ammo = 0
        health = 0
        screen.blit(labelLevelDone, (1280/2-(labelLevelDone.get_width()/2),720/2-(labelLevelDone.get_height()/2)))

    if health == 0 or ammo == 0:
        canFire = False

    #blood display
    bloodStage = 100 - health
    if bloodStage == 10:
        screen.blit(b1, (0,0))
    elif bloodStage == 20:
        screen.blit(b2, (0,0))
    elif bloodStage == 30:
        screen.blit(b3, (0,0))
    elif bloodStage == 40:
        screen.blit(b4, (0,0))
    elif bloodStage == 50:
        screen.blit(b5, (0,0))
    elif bloodStage == 60:
        screen.blit(b6, (0,0))
    elif bloodStage == 70:
        screen.blit(b7, (0,0))
    elif bloodStage == 80:
        screen.blit(b8, (0,0))
    elif bloodStage == 90:
        screen.blit(b9, (0,0))
    elif bloodStage == 100 and score < 70:
        screen.blit(b10, (0,0))
        
    pygame.display.update()

