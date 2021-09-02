import logging
import threading
import time

import pygame

import receiving

# Init Pygame Variables
WIDTH, HEIGHT = 1280, 480
BOT_WIDTH, BOT_HEIGHT = int(HEIGHT/8), int(HEIGHT/8)
FONT_SIZE = int(HEIGHT / 20)

GRAY = (44, 44, 44)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (47, 100, 220)
RED = (255, 24, 27)

ICON = 'assets/radar.png'
BOT = 'assets/bot.png'
FIELD = 'assets/ultimategoalfield.png'

FPS = 60


# Init Logging
logging.basicConfig(filename='response.log',
                    format='%(asctime)s %(levelname)s: %(message)s', level=logging.DEBUG, filemode='w')


def receive():
    receiving.recieve()


def rot_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(
        center=image.get_rect(center=(x, y)).center)
    return rotated_image, new_rect


def draw_window(WIN, font, bot, field):
    data = eval(receiving.response)
    rotation = data["Rotation"]

    WIN.fill(GRAY)
    
    pygame.draw.line(WIN, WHITE, (WIDTH/2, 0), (WIDTH/2, HEIGHT), 1)
    
    # pygame.draw.rect(WIN, WHITE, pygame.Rect(WIDTH/16, 0, HEIGHT, HEIGHT), 1)
    pygame.draw.line(WIN, RED, (WIDTH/16 - 2, 0), (WIDTH/16 - 2, HEIGHT), 8)
    pygame.draw.line(WIN, BLUE, (WIDTH/16 + HEIGHT, 0), (WIDTH/16 + HEIGHT, HEIGHT), 8)
    WIN.blit(field, (WIDTH/16, 0))

    bot, botPos = rot_center(bot, -rotation, WIDTH/8, HEIGHT - BOT_HEIGHT/2)

    WIN.blit(bot, botPos)

    rotationText = font.render(f'Rotation: {rotation}', True, WHITE)
    rotationTextRect = rotationText.get_rect(center=(WIDTH * 3/4, HEIGHT/20))
    WIN.blit(rotationText, rotationTextRect)

    MotorText = font.render('Motors:', True, WHITE)
    MotorTextRect = MotorText.get_rect(center=(WIDTH* 3/4, HEIGHT/6))
    WIN.blit(MotorText, MotorTextRect)

    for motor, placement, motorName in zip(data['Motors'], [30, 60, 90, 120], ['TL', 'TR', 'BL', 'BR']):
        MotorText = font.render(f'{motorName}: {motor}', True, WHITE)
        MotorTextRect = MotorText.get_rect(
            center=(WIDTH * 3/4, (HEIGHT/6) + (placement)))
        WIN.blit(MotorText, MotorTextRect)

    StatusText = font.render(f'Status: {data["Status"]}', True, WHITE)
    StatusTextRect = StatusText.get_rect(center=(WIDTH* 3/4, HEIGHT-FONT_SIZE))
    WIN.blit(StatusText, StatusTextRect)

    pygame.display.update()


def readout():
    pygame.font.init()

    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("Virtual Bot")
    pygame.display.set_icon(pygame.image.load(ICON))

    bot = pygame.image.load(BOT)
    bot = pygame.transform.scale(bot, (BOT_WIDTH, BOT_HEIGHT))
    
    field = pygame.image.load(FIELD)
    field = pygame.transform.scale(field, (HEIGHT, HEIGHT))

    font = pygame.font.SysFont('Calibri', FONT_SIZE)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window(WIN, font, bot, field)


def log():
    pastResponse = ''
    while True:
        time.sleep(0.01)
        response = receiving.response
        if response != pastResponse:
            logging.info(response)
            pastResponse = response


if __name__ == "__main__":
    t1 = threading.Thread(target=readout)
    t2 = threading.Thread(target=receive)
    t3 = threading.Thread(target=log)

    t2.daemon = True
    t3.daemon = True

    t1.start()
    t2.start()
    t3.start()

    t1.join()
