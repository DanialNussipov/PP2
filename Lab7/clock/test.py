"""import pygame

pygame.init()

screen_height = 600
screen_width = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Clock")


right_hand = pygame.image.load(r"C:\Users\Danial\Desktop\UNIVERSITY\PP2\Lab7\clock\rhand.png")
pivot = (400, 300)

angle = 0
center = (400, 300)

cloack = pygame.time.Clock()

running = True
while running:
     screen.fill((0,0,0))
     rotated = pygame.transform.rotate(right_hand, angle)
     rect = rotated.get_rect(center = center)
     screen.blit(rotated, rect.topleft)
     pygame.display.flip()
     angle += 2
     cloack.tick(60)
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               running = False
               
pygame.quit()"""