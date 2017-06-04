import pygame                       # here's the code import the module for using pygame functions
import time
import random
pygame.init()


display_w = 800
display_h = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

block_color = (127,127,127)

car_w = 93

gameD = pygame.display.set_mode((display_w ,display_h))
pygame.display.set_caption('Py-racing')

clock = pygame.time.Clock()         # used to work like a clock timer in the game                 

carImg = pygame.image.load('F:\Diva_miniProject\images.jpg')



def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score:" +str(count), True, black)
    gameD.blit(text , (0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameD, color, [thingx, thingy, thingw, thingh])
    

def car(x,y):
    gameD.blit(carImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_w/2),(display_h/2))
    gameD.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def crash():
    message_display('you Crashed')

def game_loop():

    x = (display_w * 0.45)
    y = (display_h * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_w)
    thing_starty =-600
    thing_speed = 5
    thing_width = 100
    thing_height = 100

    dodged = 0
    
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():                        # for the pop up window asking for the quit
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:                    # put the navigation values in keys
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0


        x += x_change

        gameD.fill(white)

        # passing the values of things
        
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed

        car(x,y)
        things_dodged(dodged)

        if x > display_w - car_w or x < 0:
            crash()

        if thing_starty > display_h:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_w)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged +1.2)


        if y < thing_starty+thing_height:
            print('y crooseover')

            if x > thing_startx and x < thing_startx + thing_width or x+car_w > thing_startx and x+car_w < thing_startx+thing_width:
                print('')
                crash()

        pygame.display.update()

        clock.tick(60)                  # this tick used to make frame updation fast and smooth





game_loop()
pygame.quit()
quit()
    
