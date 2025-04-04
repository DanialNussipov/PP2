import pygame
import sys

pygame.init()
width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Paint")

# colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
gray = (200, 200, 200)

# creating another surface for painting
canvas = pygame.Surface((width, height - 50))
canvas.fill(white)

# creating class for buttons
class Button:
     def __init__(self, x, y, width, height, text, color, action):
          self.rect = pygame.Rect(x, y, width, height)
          self.text = text
          self.color = color
          self.action = action
     # draw the button with text
     def draw(self, screen):
          pygame.draw.rect(screen, self.color, self.rect)
          font = pygame.font.Font(None, 30)
          text_surface = font.render(self.text, True, white)
          screen.blit(text_surface, (self.rect.x + 7, self.rect.y + 10))
     # check if the button was clicked and call its action
     def check_action(self, event):
          if event.type == pygame.MOUSEBUTTONDOWN:
               if self.rect.collidepoint(event.pos):
                    self.action()

drawing = False
brush_color = black
mode = "brush"
shape_start = None

# functions which will be included into buttons 
def set_black():
     global brush_color
     brush_color = black
def set_green():
     global brush_color
     brush_color = green
def set_red():
     global brush_color
     brush_color = red
def set_blue():
     global brush_color
     brush_color = blue
def erase():
     global brush_color
     brush_color = white
def clear_screen():
     canvas.fill(white)
def exit_app():
     pygame.quit()
     sys.exit()
def set_rect_mode():
     global mode
     mode = "rect"
def set_brush_mode():
     global mode
     mode = "brush"
def set_circle_mode():
     global mode
     mode = "circle"

# buttons
buttons = [
     Button(10, 10, 70, 30, "Black", black, set_black),
     Button(80, 10, 70, 30, "Green", green, set_green),
     Button(150, 10, 70, 30, "Red", red, set_red),
     Button(220, 10, 70, 30, "Blue", blue, set_blue),
     Button(290, 10, 60, 30, "Clear", gray, clear_screen),
     Button(740, 10, 50, 30, "Exit", red, exit_app),
     Button(470, 10, 60, 30, "Eraser", gray, erase),
     Button(550, 10, 60, 30, "Brush", gray, set_brush_mode),
     Button(620, 10, 90, 30, "Rectangle", gray, set_rect_mode),
     Button(350, 10, 60, 30, "Circle", gray, set_circle_mode)

]

while True:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
          
          if event.type == pygame.MOUSEBUTTONDOWN:
               if event.button == 1:
                    if mode == "brush":
                         drawing = True
                    elif mode in ["rect", "circle"]:
                         shape_start = pygame.mouse.get_pos()
          # draw shape if button is released
          if event.type == pygame.MOUSEBUTTONUP:
               if event.button == 1:
                    if mode == "brush":
                         drawing = False
                    elif mode == "rect" and shape_start:
                         end_pos = pygame.mouse.get_pos()
                         x1, y1 = shape_start
                         x2, y2 = end_pos
                         y1 -= 50
                         y2 -= 50
                         rect = pygame.Rect(
                         min(x1, x2),
                         min(y1, y2),
                         abs(x2 - x1),
                         abs(y2 - y1)
                         )
                         pygame.draw.rect(canvas, brush_color, rect, 2)
                         shape_start = None
                    elif mode == "circle" and shape_start:
                         end_pos = pygame.mouse.get_pos()
                         x1, y1 = shape_start
                         x2, y2 = end_pos
                         y1 -= 50
                         y2 -= 50
                         center = ((x1 + x2) // 2, (y1 + y2) // 2)
                         radius = int((((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5) // 2)
                         pygame.draw.circle(canvas, brush_color, center, radius, 2)
                         shape_start = None
                    
          # check if any button was clicked
          for button in buttons:
               button.check_action(event)
     # if drawing with brush, draw a small circle at the mouse position    
     if drawing and mode == "brush":
          mouse_x, mouse_y = pygame.mouse.get_pos()
          if mouse_y > 50:
               pygame.draw.circle(canvas, brush_color, (mouse_x, mouse_y - 50), 5)

     screen.fill(gray)
     screen.blit(canvas, (0, 50))
     # draw preview shape while dragging mouse (rectangle or circle)
     if shape_start and mode in ["rect", "circle"]:
          x1, y1 = shape_start
          x2, y2 = pygame.mouse.get_pos()
          y1 -= 50
          y2 -= 50
          temp_surface = canvas.copy()
          if mode == "rect":
               rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
               pygame.draw.rect(temp_surface, brush_color, rect, 2)
               screen.blit(temp_surface, (0, 50))
          if mode == "circle":
               center = ((x1 + x2) // 2, (y1 + y2) // 2)
               radius = int((((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5) // 2)
               pygame.draw.circle(temp_surface, brush_color, center, radius, 2)
          screen.blit(temp_surface, (0, 50))
     

     # draw the top button area
     pygame.draw.rect(screen, gray, (0, 0, width, 50))
     for button in buttons:
          button.draw(screen)

     pygame.display.flip()
