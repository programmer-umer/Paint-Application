import pygame
pygame.init()

HEIGHT = 700
WIDTH  = 1000

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
AQUA  = "aqua"
PINK  = "pink"

radius_of_brush = 10

font = pygame.font.SysFont('pagul', 15)
brush_sizes_text = font.render("Brush", True, BLACK)
px10_text = font.render("10PX", True, WHITE)
px30_text = font.render("30PX", True, WHITE)
px50_text = font.render("50PX", True, WHITE)

color_text = font.render("Colors", True, BLACK)

eraser_text = font.render("Eraser", True, BLACK)

save_text = font.render("Save", True, WHITE)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")
window.fill(WHITE)

CANVAS = pygame.Rect(75, 0, WIDTH-75, HEIGHT)
CANVAS_SURFACE = window.subsurface(CANVAS)

class Button:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def clicked(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height:
            return True
class Menu:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def clicked(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.x <= mouse_x <= self.x + self.width + radius_of_brush-2 and self.y <= mouse_y <= self.y + self.height:
            return True
    
px10_button = Button(10, 15+brush_sizes_text.get_height(), 50, 30)
px30_button = Button(10, 55+brush_sizes_text.get_height(), 50, 30)
px50_button = Button(10, 95+brush_sizes_text.get_height(), 50, 30)

red_button = Button(10, 102+brush_sizes_text.get_height() + 50, 50, 30)
green_button = Button(10, 102+brush_sizes_text.get_height() + 90, 50, 30)
blue_button = Button(10, 102+brush_sizes_text.get_height() + 130, 50, 30)
yellow_button = Button(10, 102+brush_sizes_text.get_height() + 170, 50, 30)
aqua_button = Button(10, 102+brush_sizes_text.get_height() + 210, 50, 30)
black_button = Button(10, 102+brush_sizes_text.get_height() + 250, 50, 30)

eraser =  Button(10, 102+brush_sizes_text.get_height() + 320, 50, 30)

save = Button(10, 102+brush_sizes_text.get_height() + 380, 50, 30)

menu = Menu(0, 0, 75, HEIGHT)
pygame.draw.rect(window, PINK, pygame.Rect(menu.x, menu.y, menu.width, menu.height))

def brush_sizes_buttons(window):
    window.blit(brush_sizes_text, (10,10))
    pygame.draw.rect(window, BLACK, pygame.Rect(px10_button.x, px10_button.y, px10_button.width, px10_button.height))
    window.blit(px10_text, (16,22+brush_sizes_text.get_height()))
    pygame.draw.rect(window, BLACK, pygame.Rect(px30_button.x, px30_button.y, px30_button.width, px30_button.height))
    window.blit(px30_text, (16,62+brush_sizes_text.get_height()))
    pygame.draw.rect(window, BLACK, pygame.Rect(px50_button.x, px50_button.y, px50_button.width, px50_button.height))
    window.blit(px50_text, (16,102+brush_sizes_text.get_height()))

def colors_buttons(window):
    window.blit(color_text, (10,102+brush_sizes_text.get_height() + 30 ))
    pygame.draw.rect(window, RED, pygame.Rect(red_button.x, red_button.y, red_button.width, red_button.height))
    pygame.draw.rect(window, GREEN, pygame.Rect(green_button.x, green_button.y, green_button.width, green_button.height))
    pygame.draw.rect(window, BLUE, pygame.Rect(blue_button.x, blue_button.y, blue_button.width, blue_button.height))
    pygame.draw.rect(window, YELLOW, pygame.Rect(yellow_button.x, yellow_button.y, yellow_button.width, yellow_button.height))
    pygame.draw.rect(window, AQUA, pygame.Rect(aqua_button.x, aqua_button.y, aqua_button.width, aqua_button.height))
    pygame.draw.rect(window, BLACK, pygame.Rect(black_button.x, black_button.y, black_button.width, black_button.height))
    window.blit(eraser_text, (10, eraser.y - 20 ))
    pygame.draw.rect(window, WHITE, pygame.Rect(eraser.x, eraser.y, eraser.width, eraser.height))
    pygame.draw.rect(window, BLACK, pygame.Rect(save.x, save.y, save.width, save.height))
    window.blit(save_text, (save.x+6, save.y+7))
def brush(window, radius, color):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if not menu.clicked():    
        pygame.draw.circle(window, color, (mouse_x, mouse_y), radius)

def main():
    global radius_of_brush
    a = 0
    color = BLACK
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if px10_button.clicked():
                    radius_of_brush = 10
                if px30_button.clicked():
                    radius_of_brush = 30
                if px50_button.clicked():
                    radius_of_brush = 50
                if red_button.clicked():
                    color = RED
                if green_button.clicked():
                    color = GREEN
                if blue_button.clicked():
                    color = BLUE
                if yellow_button.clicked():
                    color = YELLOW
                if aqua_button.clicked():
                    color = AQUA
                if black_button.clicked():
                    color = BLACK
                if eraser.clicked():
                    color = WHITE
                if save.clicked():
                    a += 1
                    filename = f"Untitled {a}.png"
                    pygame.image.save(CANVAS_SURFACE, filename)

        brush_sizes_buttons(window)
        colors_buttons(window)

        keys = pygame.mouse.get_pressed()
        if (keys[0] == True):
            brush(window, radius_of_brush, color)
       
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()