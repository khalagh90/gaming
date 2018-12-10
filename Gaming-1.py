import pygame
import time
import random
pygame.init()
#show resolation display
display_width = 800
display_height = 600
#colors
black =(0,0,0)
white = (255,255,255)
red = (255,0,0)
a = 180
b = 170
c = 255
motefareghe = (a,b,c)
#show display
gameDisplay = pygame.display.set_mode((display_width,display_height))
#show name up page
pygame.display.set_caption('Race Car')
#
clock = pygame.time.Clock()
#show car in the private location
carimg = pygame.image.load('Bug.png')
#option in with car
car_width = 57

def stuff_dodged (count):
    font = pygame.font.SysFont(None , 25)
    text = font.render("score : " +str(count),True , red)
    gameDisplay.blit(text,(0,0))



def stuff(stuffx,stuffy,stuffw,stuffh,color):
    pygame.draw.rect(gameDisplay,color,[stuffx,stuffy,stuffw,stuffh])
    

def Car(x,y):
    gameDisplay.blit(carimg,(x,y))

def text_objects(text,font):
    TextSurface= font.render(text, True ,red)
    return  TextSurface, TextSurface.get_rect()



def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',90)
    Textsurf, TextRect = text_objects(text,largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(Textsurf,TextRect)
    pygame.display.update()

    time.sleep(2)
    game_loop()


def crash ():
    message_display('YOU CRASHED')

def game_loop(): 
        x = (display_width * 0.45)
        y = (display_height * 0.8)

        x_change = 0

        stuff_startx = random.randrange(0,display_width)
        stuff_starty = -600
        stuff_speed = 2
        stuff_width = 75
        stuff_height = 75
        dodged = 0

        gameExit = False

        #event move mouse keyboard
        while not gameExit:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #gameExit = True
                    pygame.quit()
                    quit()
        #keydown keyboard 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -5
                    elif event.key == pygame.K_RIGHT:  
                        x_change = 5   
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0   
            x += x_change                      
            print(event)    

            gameDisplay.fill(white)   
            #stuffx,stuffy,stuffw,stuffh,color
  
          

            stuff(stuff_startx,stuff_starty,stuff_width,stuff_height,motefareghe)
            stuff_starty += stuff_speed
            
            stuff_dodged(dodged)

            Car(x,y) 
            #close the car in the left & right
            if x > display_width - car_width or x < 0:
                crash() 

            if stuff_starty > display_height:
                stuff_starty = 0 - stuff_height
                stuff_startx = random.randrange(0,display_width)
                dodged += 1

                if (dodged % 5 == 0):
                    stuff_speed += 2

            if y < stuff_starty + stuff_height:
                
                if x > stuff_startx and x < stuff_startx + stuff_width or x + car_width > stuff_startx and x + car_width < stuff_startx + stuff_width:
                    crash() 

            pygame.display.update()
            clock.tick(120)

game_loop()
pygame.quit()
quit()

    