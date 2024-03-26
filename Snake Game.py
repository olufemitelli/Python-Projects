import time
import random
import pygame
serpent_speed = 15

#Size of Window
window_x = 720
window_y = 480


#creating the colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


#initializing Pygame
pygame.init()

#Initializing game window
pygame.display.set_caption('PYsnakes')
game_window = pygame.display.set_mode((window_x, window_y))

#Frames per second controller
fps = pygame.time.Clock()

#Defining snake default position
snakes_position = [100,50]

#defining first parts of snakes body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50],
              ]

#dot's position
dots_position = [random.randrange(1, (window_x // 10)) * 10,
                random.randrange(1, (window_y // 10)) * 10,]

dot_spawn = True
direction = 'Right'
change_to = direction

score = 0

def show_score(choice, color, font, size):
    #creating font object score_font
    score_font = pygame.font.SysFont(font, size)

    #crete the display surface object
    #score_rectangle
    score_surface = score_font.render('Score : ' + str(score), True, color)


    #create a rectangular object for the text
    #surface object
    score_rectangle = score_surface.get_rect()

    #displaying text
    game_window.blit(score_surface, score_rectangle)

#game over function
def game_over():
    my_font= pygame.font.SysFont('times new roman', 50)

    #creating a text surface on which text
    #will be drawn
    game_over_surface = my_font.render(
        'Your score is : ' + str(score), True, red)

    game_over_rect = game_over_surface.get_rect()

    #setting position of the text
    game_over_rect.midtop = (window_x / 2, window_y / 4)

    #blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    #after 2 seconds we will quit the program
    time.sleep(2)

    #deactivating pygame library
    pygame.quit()

    #quit the program
    quit()

#main function
while True:

    #handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    #if two keys pressed simotaniously
    #directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'Right':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    #moving the snake
    if direction == 'UP':
        snakes_position[1] -= 10
    if direction == 'DOWN':
        snakes_position[1] += 10
    if direction == 'LEFT':
        snakes_position[0] -= 10
    if direction == 'RIGHT':
        snakes_position[0] += 10

    #snake body growing mechanism
    #if dots and snakes collide then scores will be increase by 10
    snake_body.insert(0, list(snakes_position))
    if snakes_position[0] == dots_position[0] and snakes_position[1] == dots_position[1]:
        score += 10
        dot_spawn = False
    else:
        snake_body.pop()

    if not dot_spawn:
        dots_position = [random.randrange(1, (window_x // 10)) * 10,
                         random.randrange(1, (window_y // 10)) * 10]

    fruit_spawn = True
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        dots_position[0], dots_position[1], 10, 10))

    #game over conditions
    if snakes_position[0] < 0 or snakes_position[0] > window_x - 10:
        game_over()
    if snakes_position[0] < 0 or snakes_position[0] > window_x - 10:
        game_over()

    #displaying score continuously
    show_score(1, white, 'times new roman', 20)

    #refresh game screen
    pygame.display.update()

    #fps/refresh rate
    fps.tick(snake_speed)