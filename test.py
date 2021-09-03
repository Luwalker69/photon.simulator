import math
import pygame
import pygame.draw

pygame.init()
size = 800
radius = 150
taille_fenetre = (size, size)
screen_surface = pygame.display.set_mode(taille_fenetre)
screen_surface.fill((255, 255, 255))
screen_surface.fill((255, 255, 255))
x_center, y_center = size / 2, size / 2


def quit_o(continuer):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        else:
            continuer = True
    return continuer


def changeangle(angle, teta):
    angle = angle + 180 - 2 * teta
    return angle


def angle_(x, y, angle):
    x_rad = (math.cos(math.radians(angle)))
    y_rad = (math.sin(math.radians(angle)))

    x = x + x_rad
    y = y - y_rad

    return x, y


def limit(x, y, angle):
    x_rad = (math.cos(math.radians(angle)))
    y_rad = (math.sin(math.radians(angle)))
    x = x + x_rad
    y = y - y_rad

    if math.sqrt((x_center - x) ** 2 + (y_center - y) ** 2) < radius:
        return True
    else:
        return False


def out(x, y, radius):
    if math.sqrt((x_center - x) ** 2 + (y_center - y) ** 2) == radius-2 and (x > x_start - 10 or x < x_start + 10):
        return True
    return False


continuer = True
x_start = x_center
y_start = y_center + radius
angle = 65
teta = 90 - angle
x, y = x_start, y_start

while continuer:
    continuer = quit_o(continuer)
    pygame.display.flip()
    valid = limit(x, y, angle)
    if valid:
        x, y = angle_(x, y, angle)
    else:
        angle = changeangle(angle, teta)
    if out(x, y, radius):
        continuer = False
    pygame.draw.circle(screen_surface, (255, 0, 0), (x_center, y_center), radius, width=1)
    pygame.draw.line(screen_surface, (0, 0, 255), (x, y), (x, y), 2)


