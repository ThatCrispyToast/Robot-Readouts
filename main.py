import threading
import receiving
import pygame

# Default: 700
WIDTH, HEIGHT = 800, 600
FPS = 60

def draw_window(WIN, font):
    textsurface = font.render(receiving.response, True, (255, 255, 255))
    text_rect = textsurface.get_rect(center=(WIDTH/2, HEIGHT-15))
    WIN.fill((18, 18, 18))
    WIN.blit(textsurface, text_rect)
    pygame.display.update()


def main():
    pygame.font.init()
    
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("Virtual Bot")
    pygame.display.set_icon(pygame.image.load('assets/radar.png'))
    
    font = pygame.font.SysFont('Calibri', 30)
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        draw_window(WIN, font)
        
def recieve():
    receiving.recieve()

if __name__ == "__main__":
    t1 = threading.Thread(target=main)
    t2 = threading.Thread(target=recieve)
    t2.daemon = True
  
    t1.start()
    t2.start()

    t1.join()
    
    