import pygame

WHITE = (255, 255, 255)
CRIMSON = (220, 20, 60)

pygame.init()

screen_width = 750
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ball")

RADIUS = 25
STEP = 20
x, y = screen_width / 2, screen_height / 2

clock = pygame.time.Clock()
running = True
while running:
     
     screen.fill(WHITE)
     pygame.draw.circle(screen, CRIMSON, (x, y), RADIUS)
     
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               running = False
     keys = pygame.key.get_pressed()
     
     if keys[pygame.K_UP]  and y - STEP - RADIUS >= 0:
                    y -= STEP
     if keys[pygame.K_DOWN] and y + STEP + RADIUS <= screen_height:
                    y += STEP
     if keys[pygame.K_RIGHT] and x + STEP + RADIUS <= screen_width:
                    x += STEP
     if keys[pygame.K_LEFT] and x - STEP - RADIUS >= 0: 
                    x -= STEP
                    
     pygame.display.flip()
     clock.tick(30)
     
pygame.quit()
     