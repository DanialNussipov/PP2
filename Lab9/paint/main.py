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
canvas = pygame.Surface((width, height - 100))
canvas.fill(white)

# creating class for buttons
class Button:
    def __init__(self, x, y, width, height, text, color, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.action = action

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 30)
        text_surface = font.render(self.text, True, white)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

    def check_action(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()

drawing = False
brush_color = black
mode = "brush"
shape_start = None

# mode functions
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

def set_brush_mode():
    global mode
    mode = "brush"

def set_rect_mode():
    global mode
    mode = "rect"

def set_circle_mode():
    global mode
    mode = "circle"

def set_square_mode():
    global mode
    mode = "square"

def set_rtriangle_mode():
    global mode
    mode = "rtriangle"

def set_eqtriangle_mode():
    global mode
    mode = "eqtriangle"

def set_rhombus_mode():
    global mode
    mode = "rhombus"

# buttons
buttons = [
    # row 1
    Button(10, 10, 70, 30, "Black", black, set_black),
    Button(80, 10, 70, 30, "Green", green, set_green),
    Button(150, 10, 70, 30, "Red", red, set_red),
    Button(220, 10, 70, 30, "Blue", blue, set_blue),
    Button(290, 10, 70, 30, "Clear", gray, clear_screen),
    Button(740, 10, 50, 30, "Exit", red, exit_app),
    Button(350, 10, 70, 30, "Eraser", gray, erase),
    Button(420, 10, 70, 30, "Brush", gray, set_brush_mode),
    Button(420, 50, 90, 30, "Rect", gray, set_rect_mode),
    Button(470, 50, 80, 30, "Circle", gray, set_circle_mode),
    Button(10, 50, 80, 30, "Square", gray, set_square_mode),
    Button(90, 50, 90, 30, "R-Triangle", gray, set_rtriangle_mode),
    Button(200, 50, 100, 30, "Eq-Triangle", gray, set_eqtriangle_mode),
    Button(320, 50, 90, 30, "Rhombus", gray, set_rhombus_mode),
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
                elif mode in ["rect", "circle", "square", "rtriangle", "eqtriangle", "rhombus"]:
                    shape_start = pygame.mouse.get_pos()
        # draw shape if button is released
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if mode == "brush":
                    drawing = False
                elif shape_start:
                    x1, y1 = shape_start
                    x2, y2 = pygame.mouse.get_pos()
                    y1 -= 100
                    y2 -= 100
                    
                    # a rectangle is defined by the top-left corner and the absolute width and height.
                    if mode == "rect":
                        rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
                        pygame.draw.rect(canvas, brush_color, rect, 2)
                    # a square uses the minimum side length between width and height to ensure equal sides.
                    elif mode == "square":
                        side = min(abs(x2 - x1), abs(y2 - y1))
                        rect = pygame.Rect(x1, y1, side, side)
                        pygame.draw.rect(canvas, brush_color, rect, 2)
                    # a circle is drawn using the center point and radius calculated from the distance between start and end points.
                    elif mode == "circle":
                        center = ((x1 + x2) // 2, (y1 + y2) // 2)
                        radius = int((((x2 - x1)**2 + (y2 - y1)**2) ** 0.5) // 2)
                        pygame.draw.circle(canvas, brush_color, center, radius, 2)
                    # a right triangle is formed using the start point, end point, and a third point aligned horizontally or vertically.
                    elif mode == "rtriangle":
                        points = [(x1, y1), (x1, y2), (x2, y2)]
                        pygame.draw.polygon(canvas, brush_color, points, 2)
                    # an an equilateral triangle, half of the base equals height divided by sqrt(3).
                    elif mode == "eqtriangle":
                        height = abs(y2 - y1)
                        half_base = int(height / (3 ** 0.5))
                        top = ((x1 + x2) // 2, y1)
                        left = (top[0] - half_base, y2)
                        right = (top[0] + half_base, y2)
                        pygame.draw.polygon(canvas, brush_color, [top, left, right], 2)
                    # a rhombus is defined by its diagonals, with vertices at the top, right, bottom, and left from the center point.
                    elif mode == "rhombus":
                        center_x = (x1 + x2) // 2
                        center_y = (y1 + y2) // 2
                        dx = abs(x2 - x1) // 2
                        dy = abs(y2 - y1) // 2
                        points = [
                            (center_x, center_y - dy),
                            (center_x + dx, center_y),
                            (center_x, center_y + dy),
                            (center_x - dx, center_y)
                        ]
                        pygame.draw.polygon(canvas, brush_color, points, 2)
                    shape_start = None
        # check if any button was clicked
        for button in buttons:
            button.check_action(event)
    # if drawing with brush, draw a small circle at the mouse position    
    if drawing and mode == "brush":
        mx, my = pygame.mouse.get_pos()
        if my > 100:
            pygame.draw.circle(canvas, brush_color, (mx, my - 100), 5)

    screen.fill(gray)
    screen.blit(canvas, (0, 100))
    # draw preview shape while dragging mouse (rectangle or circle)
    if shape_start and mode in ["rect", "circle", "square", "rtriangle", "eqtriangle", "rhombus"]:
        x1, y1 = shape_start
        x2, y2 = pygame.mouse.get_pos()
        y1 -= 100
        y2 -= 100
        temp_surface = canvas.copy()
        if mode == "rect":
            rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
            pygame.draw.rect(temp_surface, brush_color, rect, 2)
            
        elif mode == "square":
            side = max(abs(x2 - x1), abs(y2 - y1))
            rect = pygame.Rect(x1, y1, side, side)
            pygame.draw.rect(temp_surface, brush_color, rect, 2)
            
        elif mode == "circle":
            center = ((x1 + x2) // 2, (y1 + y2) // 2)
            radius = int((((x2 - x1)**2 + (y2 - y1)**2) ** 0.5) // 2)
            pygame.draw.circle(temp_surface, brush_color, center, radius, 2)
            
        elif mode == "rtriangle":
            points = [(x1, y1), (x1, y2), (x2, y2)]
            pygame.draw.polygon(temp_surface, brush_color, points, 2)
            
        elif mode == "eqtriangle":
            height = abs(y2 - y1)
            half_base = int(height / (3 ** 0.5))
            top = ((x1 + x2) // 2, y1)
            left = (top[0] - half_base, y2)
            right = (top[0] + half_base, y2)
            pygame.draw.polygon(temp_surface, brush_color, [top, left, right], 2)
            
        elif mode == "rhombus":
            center_x = (x1 + x2) // 2
            center_y = (y1 + y2) // 2
            dx = abs(x2 - x1) // 2
            dy = abs(y2 - y1) // 2
            points = [
                (center_x, center_y - dy),
                (center_x + dx, center_y),
                (center_x, center_y + dy),
                (center_x - dx, center_y)
            ]
            pygame.draw.polygon(temp_surface, brush_color, points, 2)
            
        screen.blit(temp_surface, (0, 100))
    # draw the top button area
    pygame.draw.rect(screen, gray, (0, 0, width, 100))
    for button in buttons:
        button.draw(screen)

    pygame.display.flip()
