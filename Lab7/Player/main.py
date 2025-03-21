import pygame

GRAY = (220, 220, 220)
CRIMSON = (220, 20, 60)
LIGHT_SALMON = (255, 160, 122)
WHITE = (255, 255, 255)
DARK_RED = (139, 0, 0)

def run():
     
     pygame.init()
     
     screen_width = 600
     screen_heigth = 300
     
     screen = pygame.display.set_mode((screen_width, screen_heigth))
     pygame.display.set_caption("Music Player")
     
     playlist  = [
          r"C:\Users\Danial\Desktop\UNIVERSITY\PP2\Lab7\Player\songs\Linkin Park - Breaking The Habit.mp3",
          r"C:\Users\Danial\Desktop\UNIVERSITY\PP2\Lab7\Player\songs\Arctic Monkeys - R U Mine.mp3",
          r"C:\Users\Danial\Desktop\UNIVERSITY\PP2\Lab7\Player\songs\Linkin Park - Numb.mp3",
          r"C:\Users\Danial\Desktop\UNIVERSITY\PP2\Lab7\Player\songs\Post Malone - Circles.mp3",
          r"C:\Users\Danial\Desktop\UNIVERSITY\PP2\Lab7\Player\songs\Eminem - Houdini.mp3",
          r"C:\Users\Danial\Desktop\UNIVERSITY\PP2\Lab7\Player\songs\Нервы - Так Как Надо.mp3"
     ]
     
     current_track = 0
     pygame.mixer.init()
     pygame.mixer.music.load(playlist[current_track])
     
     def play_track(index):
          pygame.mixer.music.load(playlist[index])
          pygame.mixer.music.play()
          
     running = True
     paused = False
     font = pygame.font.Font(None, 36)
     
     while running:
          
          for event in pygame.event.get():
               
               if event.type == pygame.QUIT:
                    running = False
               elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                         if pygame.mixer.music.get_busy():
                              pygame.mixer.music.pause()
                              paused = True
                         elif paused:
                              pygame.mixer.music.unpause()
                              paused = False
                    elif event.key == pygame.K_d:
                         current_track = (current_track + 1) % len(playlist)
                         """
                         current_track = 0 --> (0 + 1) % 4 = 1 --> means that next song w index 1 etc.
                         current_track = 1 --> (1 + 1) % 4 = 2 --> next song w index 2 etc.
                         """
                         play_track(current_track)
                    elif event.key == pygame.K_a:
                         current_track = (current_track - 1) % len(playlist)
                         """ 
                         current_track = 0 --> (0 - 1) % 4 = 3 --> if we start from first song it will play the last one
                         """
                         play_track(current_track)
          
          screen.fill(LIGHT_SALMON)
                         
          prev = pygame.Rect(25, 100, 150, 75)
          pause = pygame.Rect(227, 100, 150, 75)
          next = pygame.Rect(425, 100, 150, 75)
          
          pygame.draw.rect(screen, CRIMSON, prev, border_radius = 15)
          pygame.draw.rect(screen, CRIMSON, pause, border_radius = 15)
          pygame.draw.rect(screen, CRIMSON, next, border_radius = 15)
          
          prev_text = font.render("Prev(A)", True, DARK_RED)
          pause_text = font.render("Pause", True, DARK_RED)
          pause_text2 = font.render("(Space)", True, DARK_RED)
          next_text = font.render("Next(D)", True, DARK_RED)

          screen.blit(prev_text, (prev.x + 33, prev.y + 20))
          screen.blit(pause_text, (pause.x + 33, pause.y + 10))
          screen.blit(pause_text2, (pause.x + 27, pause.y + 35))
          screen.blit(next_text, (next.x + 33, next.y + 20))
          
          pygame.display.flip()
     pygame.quit()
     
run()
                         
                    
          