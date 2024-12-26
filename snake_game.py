import pygame as pg
import random
pg.init()
pg.mixer.init()
# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0,255,0)

# specifing the game window 
screen_width = 1200
screen_height = 600
game_display = pg.display.set_mode((screen_width, screen_height))

#backgroung image
back = pg.image.load("rb_35589.png")
back = pg.transform.scale(back,(screen_width,screen_height)).convert_alpha()
# snake back ground
bcsnake = pg.image.load("snake.png")
bcsnake = pg.transform.scale(bcsnake,(400,400)).convert_alpha()

# Game Title
pg.display.set_caption("Snakes game")
pg.display.update()
clock = pg.time.Clock()
font = pg.font.SysFont(None, 55)

# funciton for printing the score ont the screen 
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_display.blit(screen_text, [x,y])

# function to make snake 
def plot_snake(gameWindow, color, snake_list, snake_size):
    for x,y in snake_list:
        pg.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome_screen():
    pg.mixer.music.load('backgroung.mp3')
    pg.mixer.music.play()
    exit_game = False
    while not exit_game:
        game_display.fill(black)
        game_display.blit(bcsnake,(400,100))
        text_screen("welcome to the snake game", red, 350,200,)
        text_screen("START THE GAME (ENTER)", red, 350,280)
        text_screen("EXIT GAME (BACKSPACE)", red, 350,340)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit_game = True
            
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    game_loop()
                if event.key == pg.K_BACKSPACE:
                    exit_game = True
        pg.display.update()
        clock.tick(60)
# game loop function 
def game_loop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 40
    snake_y = 40
    velocity_x = 0
    velocity_y = 0
    snake_list = []
    snake_length = 1
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    food_x = random.randint(300, 900)
    food_y = random.randint(200, 500)
    score = 0
    init_velocity = 5
    snake_size = 30
    fps = 60
    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            game_display.fill(black)
            text_screen("OOP's YOU HAVE COLLIDE !", red, 300, 200)
            text_screen("PRESS  ENTER  TO START THE GAME AGAIN", red, 200, 250)

            for event in pg.event.get():
                # use for quiting the game 
                if event.type == pg.QUIT:
                    exit_game = True

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        game_loop()
                    if event.key == pg.K_BACKSPACE:
                        exit_game = True
        else:
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit_game = True

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pg.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pg.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pg.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                pg.mixer.music.load("mr_munch.mp3")
                pg.mixer.music.play()
                score +=5
                food_x = random.randint(300, 900)
                food_y = random.randint(200, 500)
                snake_length +=5
                if score > int(hiscore):
                    hiscore = score

            game_display.fill(black)
            game_display.blit(back,(0,0))
            text_screen(f"score: {score}", red, 5, 5)
            text_screen(f"hiscore: {hiscore}", red, 900, 5)
            pg.draw.rect(game_display, red, [food_x, food_y, 20, 20])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True
                pg.mixer.music.load("gameover.mp3")
                pg.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pg.mixer.music.load("gameover.mp3")
                pg.mixer.music.play()
            plot_snake(game_display, green, snake_list, snake_size)
        pg.display.update()
        clock.tick(fps)

    pg.quit()
    quit()
# game_loop()
welcome_screen()

