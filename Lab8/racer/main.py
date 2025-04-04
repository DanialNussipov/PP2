import pygame, sys, random

# colors
black = (0, 0, 0)
white = (255, 255, 255)

pygame.init()
width, height = 270, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Racer")

# uploading images
track = pygame.image.load(r"C:\Users\Danial\Desktop\UNIVERSITY\PP2\Lab8\racer\track.png")
car = pygame.image.load(r"C:\Users\Danial\Desktop\UNIVERSITY\PP2\Lab8\racer\car.png")
coin = pygame.image.load(r"C:\Users\Danial\Desktop\UNIVERSITY\PP2\Lab8\racer\coin.png")
enemy_car = pygame.image.load(r"C:\Users\Danial\Desktop\UNIVERSITY\PP2\Lab8\racer\enemy_car.png")

# coordinates for car, coin and enemy car
car_x = width // 2 - 20
car_y = height - 100
car_speed = 5

coin_x = random.randint(20, 250)
coin_y = -30

enemy_car_x = random.randint(20, 250)
enemy_car_y = - 100

# variables for coins, score and font
score = 0
coins = 0
font = pygame.font.Font(None, 16)

# main loop
running = True

clock = pygame.time.Clock()
while running:
     # FPS
     clock.tick(60)
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               running = False
               sys.exit()
     # movement elements
     keys = pygame.key.get_pressed()
     if keys[pygame.K_RIGHT] and car_x < width - 60:
          car_x += car_speed
     if keys[pygame.K_LEFT] and car_x > 17:
          car_x -= car_speed
     
     # generating coins randomly     
     coin_y += 5
     if coin_y > height:
          coin_y = -30
          coin_x = random.randint(20, 250)
          
     # generating cars randomly
     enemy_car_y += 10
     if enemy_car_y > height:
          enemy_car_x = random.randint(20, 190)
          enemy_car_y = - 100
          score += 1
          
     # creating rects from cars and coins to check whether it collapse
     car_rect = pygame.Rect(car_x, car_y, car.get_width(), car.get_height())
     coin_rect = pygame.Rect(coin_x, coin_y, coin.get_width(), coin.get_height())
     enemy_car_rect = pygame.Rect(enemy_car_x, enemy_car_y, enemy_car.get_width(), enemy_car.get_height())
     
     # checking if car get coin
     if car_rect.colliderect(coin_rect):
          coins += 1
          coin_y = -30
          coin_x = random.randint(20, 250)
     # checking if car collapsed with another car
     if car_rect.colliderect(enemy_car_rect):
          gameover = pygame.image.load(r"C:\Users\Danial\Desktop\UNIVERSITY\PP2\Lab8\racer\gameover.png")
          screen.blit(gameover, (-30, -30))
          pygame.display.flip()
          pygame.time.delay(2000)
          pygame.quit()
          sys.exit()
     
     # show the pics
     screen.blit(track, (0, 0))
     screen.blit(car, (car_x, car_y))
     screen.blit(coin, (coin_x, coin_y))
     screen.blit(enemy_car, (enemy_car_x, enemy_car_y))
     
     # show the text
     coins_text = font.render(f"Coins: {coins}", True, white)
     score_text = font.render(f"Score: {score}", True, white)
     screen.blit(coins_text, (width - 60, 10))
     screen.blit(score_text, (width - 60, 25))
     
     # update screen
     pygame.display.flip()