import pygame
import sys

# Initializing pygame constructor
pygame.init()

# Screen resolution *Can be changed*
res = (800, 600)
# Setting up the window
screen = pygame.display.set_mode(res)

# Colors of the font, background, rectangle
color = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)
color_black = (0, 0, 0)

# Setting the width and height into a variables
width = screen.get_width()
height = screen.get_height()

# defining and rendering a text in this font.
smallfont = pygame.font.SysFont('Corbel', 40)
quitText = smallfont.render('Quit', True, color)
playText = smallfont.render('Play', True, color)

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()

        # Checking if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:
            # Play Button
            if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                print("Play game")
                break
            # Quit Button
            if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2+80:
                pygame.quit()
                sys.exit()

    # Putting background color as black
    screen.fill(color_black)

    # tuple of (x,y) coordinates where the mouse is.
    mouse = pygame.mouse.get_pos()

    # Mouse hovering over a rectangle => changes the color to light color.
    # Play rectangle
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
        pygame.draw.rect(screen, color_light, [width/2, height/2, 140, 40])
    # Quit rectangle
    elif width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+80:
        pygame.draw.rect(screen, color_light, [width/2, height/2+40, 140, 40])
    # If no rectangle is hovered on => changes back to dark color.
    else:
        pygame.draw.rect(screen, color_dark, [width/2+40, height/2, 140, 40])

    # Setting the text on the screen
    # Play Text
    screen.blit(playText, (width/2, height/2))
    # Quit Text
    screen.blit(quitText, (width/2, height/2+40))

    # Updating the frames of the game
    pygame.display.update()
