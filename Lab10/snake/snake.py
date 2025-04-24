import pygame, sys, random, psycopg2

conn = psycopg2.connect(
     host="localhost",
     dbname="lab10",
     user="postgres",
     password="pingvinkrut"
)
cur = conn.cursor()

def get_or_create_user(username):
     cur.execute("SELECT user_id FROM users WHERE username = %s", (username,))
     user = cur.fetchone()
     if user:
          user_id = user[0]
          cur.execute("SELECT score, level, coins_eaten FROM user_score WHERE user_id = %s", (user_id,))
          result = cur.fetchone()
          if result:
              return user_id, result[0], result[1], result[2]
          else:
              cur.execute("INSERT INTO user_score (user_id, score, level, coins_eaten) VALUES (%s, %s, %s, %s)", (user_id, 0, 1, 0))
              conn.commit()
              return user_id, 0, 1, 0
     else:
          cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING user_id", (username,))
          user_id = cur.fetchone()[0]
          cur.execute("INSERT INTO user_score (user_id, score, level, coins_eaten) VALUES (%s,%s, %s, %s)", (user_id, 0, 1, 0))
          conn.commit()
          return user_id, 0, 1, 0

def save_state(user_id, score, level, coins_eaten):
     cur.execute("UPDATE user_score SET score = %s, level = %s, coins_eaten = %s WHERE user_id = %s", (score, level, coins_eaten, user_id))
     conn.commit()

username = input("Введите ваше имя пользователя: ")
user_id, score, level, coins_eaten = get_or_create_user(username)

pygame.init()

width, height = 500, 500
cell_size = 10

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple snake")

# RGB colors
black = (0, 0, 0)
blue = (0, 0, 255)
BlanchedAlmond = (255, 235, 205)
Chocolate = (210, 105, 30)
NavajoWhite = (255, 222, 173)
gray = (200, 200, 200)
brown = (255, 165, 0)
red = (255, 0, 0)

# snake's head position
snake_pos = [100, 100]
snake_body = [[100, 100], [90, 100], [80, 100]]
direction = "RIGHT"
change_to = direction
# start snake's body (3 parts)
speed = 10 + (level - 1) * 2

# now i am going to create function to generate coins
def generate_coin():
     while True:
          # creating list with future coin position
          # making spawning logic
          x = random.randint(1, (width // cell_size) - 2) * cell_size
          y = random.randint(4, (height // cell_size) - 2) * cell_size
          coin = [x, y]
          # 500 - width // 10 - cell size = 50 cells in row
          # indexation starts with 0, so (0, 49)
          if coin not in snake_body:
               weight = random.choice([1, 2, 3])
               return coin, weight


def pause_game():
     paused = True
     save_state(user_id, score, level, coins_eaten)
     while paused:
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    save_state(user_id, score, level, coins_eaten)
                    pygame.quit()
                    sys.exit()
               elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                         paused = False
# creating death screen
def game_over_screen():
     screen.fill(NavajoWhite)
     font = pygame.font.Font(None, 50)
     font2 = pygame.font.Font(None, 25)
     game_over = font.render("Game over", True, black)
     restart = font2.render("Press 'R' to restart", True, black)
     # centeralize text
     screen.blit(game_over, (width // 2 - 100, height // 3))
     screen.blit(restart, (width // 2 - 75, height // 2))
     pygame.display.flip()

     waiting = True
     while waiting:
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    save_state(user_id, score, level, coins_eaten)
                    pygame.quit()
                    sys.exit()
                    # if type r - restart game
               elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                         waiting = False

# function uses global vars to change it globally and restart the game properly
def restart_game():
     global snake_pos, snake_body, direction, score, level, speed, coin_pos, running, change_to, coins_eaten
     snake_pos = [100, 100]
     direction = "RIGHT"
     change_to = "RIGHT"

     length = 3 + coins_eaten
     snake_body = []
     for i in range(length):
          snake_body.append([snake_pos[0] - i * cell_size, snake_pos[1]])

     speed = 10 + (level - 1) * 2
     coin_pos, coin_weight = generate_coin()
     running = True

# creating first coin
coin_pos, coin_weight = generate_coin()
coin_spawn = True
# saving time to compare lately
coin_timer_start = pygame.time.get_ticks()

running = True
clock = pygame.time.Clock()

while True:
     while running:
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    save_state(user_id, score, level, coins_eaten)
                    pygame.quit()
                    sys.exit()
               # moving elements
               elif event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_UP or event.key == pygame.K_w) and direction != "DOWN":
                         change_to = "UP"
                    elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and direction != "UP":
                         change_to = "DOWN"
                    elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and direction != "RIGHT":
                         change_to = "LEFT"
                    elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and direction != "LEFT":
                         change_to = "RIGHT"
                    elif event.key == pygame.K_p:
                         pause_game()

          direction = change_to

          # moving snake's head in right direction
          if direction == "UP":
               snake_pos[1] -= cell_size
          elif direction == "DOWN":
               snake_pos[1] += cell_size
          elif direction == "LEFT":
               snake_pos[0] -= cell_size
          elif direction == "RIGHT":
               snake_pos[0] += cell_size

          # check whether it collapse with border 
          if snake_pos[0] < 0 or snake_pos[0] >= width or snake_pos[1] < 30 or snake_pos[1] >= height:
               game_over_screen()
               restart_game()
               break

          # inserting new position to snake's body.
          # it means that list with snake's body position increases -> body is increasing too
          snake_body.insert(0, list(snake_pos))

          # if snake eat food body++, if not body = body
          if snake_pos == coin_pos:
               score += coin_weight
               coins_eaten += 1
               coin_spawn = False
               # every 4 points increasing the speed
               level = score // 4 + 1
               speed = 10 + (level - 1) * 2
          else:
               snake_body.pop()

          # creating new food if there is no one
          if not coin_spawn:
               # if we ate we save new time to compare with next
               coin_pos, coin_weight = generate_coin()
               coin_timer_start = pygame.time.get_ticks()
          coin_spawn = True

          # if snake collapse itself => game over
          if snake_pos in snake_body[1:]:
               game_over_screen()
               restart_game()
               break

          # if 5 seconds gone - coin disappears
          if pygame.time.get_ticks() - coin_timer_start > 5000:
               coin_spawn = False
          # making background 
          screen.fill(NavajoWhite)
          # drawing the snake
          for block in snake_body:
               pygame.draw.rect(screen, blue, pygame.Rect(block[0], block[1], cell_size, cell_size))
          # drawing the coins 
          coin_colors = {
               1: Chocolate,
               2: red,
               3: brown
          }
          pygame.draw.rect(screen, coin_colors[coin_weight], pygame.Rect(coin_pos[0], coin_pos[1], cell_size, cell_size))
          pygame.draw.rect(screen, gray, pygame.Rect(0, 0, 500, 30))
          # creating a counter for level and score
          font = pygame.font.Font(None, 24)
          score_text = font.render(f"Score: {score}  Level: {level}", True, black)
          another = font.render("To load process die & restart the game", True, black)
          screen.blit(score_text, (10, 10))
          screen.blit(another, (170, 10))
          # control game speed
          pygame.display.flip()
          clock.tick(speed)

pygame.quit()
