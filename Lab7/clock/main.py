import pygame
import datetime

pygame.init()

screen_height = 600
screen_width = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Clock")

background = pygame.image.load(r"C:\Users\Danial\Desktop\UNIVERSITY\PP2\Lab7\clock\bg.jpg")
min_hand = pygame.image.load(r"C:\Users\Danial\Desktop\UNIVERSITY\PP2\Lab7\clock\rhand.png")
sec_hand = pygame.image.load(r"C:\Users\Danial\Desktop\UNIVERSITY\PP2\Lab7\clock\lhand.png")

center = (screen_width // 2, screen_height // 2)
clock = pygame.time.Clock()

def rotating(surface, image, angle, position):
     rotated_image = pygame.transform.rotate(image, angle)
     new_rect = rotated_image.get_rect(center = position)
     surface.blit(rotated_image, new_rect.topleft)

running = True
while running:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               running = False
               
     now = datetime.datetime.now()
     second = -now.second * 6
     minute = -(now.minute * 6 + now.second * 0.1)
               
     screen.blit(background, (0, 0))

     rotating(screen, min_hand, minute, center)
     rotating(screen, sec_hand, second, center)
     
     pygame.display.flip()
     clock.tick(60)
     
pygame.quit()