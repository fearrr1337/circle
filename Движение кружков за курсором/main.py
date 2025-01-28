import pygame
import random
import math

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Круги за курсором")

num_circles = 10
circles = []
for i in range(num_circles):
    circles.append({
        'x': random.randint(50, width - 50),
        'y': random.randint(50, height - 50),
        'radius': random.randint(10, 30),
        'color': (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
        'speed': random.uniform(2, 5)
    })

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for circle in circles:
                    dx = circle['x'] - mouse_x
                    dy = circle['y'] - mouse_y
                    distance = math.hypot(dx, dy)
                    if distance < circle['radius'] * 2:
                        if distance > 0 :
                            dx /= distance
                            dy /= distance
                        circle['x'] += dx * circle['speed'] * 100
                        circle['y'] += dy * circle['speed'] * 100


    mouse_x, mouse_y = pygame.mouse.get_pos()

    for circle in circles:
        dx = mouse_x - circle['x']
        dy = mouse_y - circle['y']
        distance = math.hypot(dx, dy)
        if distance > 0:
            dx /= distance
            dy /= distance
        circle['x'] += dx * circle['speed'] / 20
        circle['y'] += dy * circle['speed'] / 20

    screen.fill((0, 0, 0))
    for circle in circles:
        pygame.draw.circle(screen, circle['color'], (int(circle['x']), int(circle['y'])), circle['radius']) # int для целых координат
    pygame.display.flip()

pygame.quit()

