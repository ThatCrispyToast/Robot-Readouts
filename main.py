import threading
import receiving
import pygame

# Default: 700
WIDTH, HEIGHT = 800, 600
FONT_SIZE = 30
GRAY = (18, 18, 18)
WHITE =(255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

def rot_center(image, angle, x, y):
    
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)

    return rotated_image, new_rect

def draw_window(WIN, font, bot):
    data = eval(receiving.response)
    rotation = data["Rotation"]
    
    WIN.fill(GRAY)
    
    bot, botPos = rot_center(bot, -rotation, WIDTH/2, HEIGHT/2)
    
    WIN.blit(bot, botPos)
    
    rotationText = font.render(f'Rotation: {rotation}', True, WHITE)
    rotationTextRect = rotationText.get_rect(center=(WIDTH/2, HEIGHT/20))
    WIN.blit(rotationText, rotationTextRect)
    
    MotorText = font.render('Motors:', True, WHITE)
    MotorTextRect = MotorText.get_rect(center=(WIDTH/11, HEIGHT/6))
    WIN.blit(MotorText, MotorTextRect)
    
    for motor, placement, motorName in zip(data['Motors'], [30, 60, 90, 120], ['TL', 'TR', 'BL', 'BR']):
        MotorText = font.render(f'{motorName}: {motor}', True, WHITE)
        MotorTextRect = MotorText.get_rect(center=(WIDTH/11, (HEIGHT/6) + (placement)))
        WIN.blit(MotorText, MotorTextRect)
    
    pygame.display.update()


def main():
    pygame.font.init()
    
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("Virtual Bot")
    pygame.display.set_icon(pygame.image.load('assets/radar.png'))
    
    bot = pygame.image.load("assets/bot.png")
    
    font = pygame.font.SysFont('Calibri', FONT_SIZE)
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        draw_window(WIN, font, bot)
        
def recieve():
    receiving.recieve()

if __name__ == "__main__":
    t1 = threading.Thread(target=main)
    t2 = threading.Thread(target=recieve)
    t2.daemon = True
  
    t1.start()
    t2.start()

    t1.join()
