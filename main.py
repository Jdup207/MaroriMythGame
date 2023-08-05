# Platformer demo for Yr11DGTA 
# James du Preez
# 1_1
# 02 August 2023
# TODO: Create main game window. Create first sprite. Bind keys for movements.
# Features implemented:

 

import pygame

pygame.init()

clock = pygame.time.Clock()

# Setting the size of the display window

win = pygame.display.set_mode((500, 500))

 

# Setting a caption for the game

pygame.display.set_caption("Demo Yr11 Platformer")

 

# Set co-ordinates of where the sprite will appear
# Set the height and width of the sprite

x = 50
y = 50
width = 20
height = 20

 
# Set velocity to control speed pf sprite
vel = 0.5

 
# Game loop starts
done = True
while done:

    pygame.time.delay(100)

 
    # Quit the game when the window gets closed

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            done = False

 

    # Movement code
    # character for as long as the key gets pressed down
    # Set up a list to do this

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    if keys[pygame.K_ESCAPE]:
         done = False

 

    # Draw over the rectangle to cover up its tracks
    win.fill((0,0,0))

 
    # Draw a rectangle which will represent the character in my game
    # win = window we draw on, RGB values, rectangle with x y width height
    pygame.draw.rect(win, (255,0,255), (x, y, width, height))

    
    # update the screen otherwise nothing draws
    pygame.display.update()
    clock.tick(250) # allows to change frame rate 

 
pygame.quit()
