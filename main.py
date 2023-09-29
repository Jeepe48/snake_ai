import pygame
import random

winSize = (600, 600)
fps = 5

apple_size = 10
snake_size = 20

borders = winSize[0] // snake_size, winSize[1] // snake_size
start_pos = borders[0] // 2, borders[1] // 2

snake = [start_pos]
tail = snake[1:]

alive = True
direction = 0
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
apple = random.randint(0, borders[0]-1), random.randint(0, borders[1]-1)

pygame.font.init()
font_gameover = pygame.font.SysFont("Arial", 45)
font_space = pygame.font.SysFont("Arial", 18)

# Цвета (R, G, B)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode(winSize)
clock = pygame.time.Clock()

running = True
while running:
    pygame.display.set_caption(f'Snake AI Score:{len(snake)}')
    pygame.display.update()
    pygame.display.flip()
    pygame.time.delay(10)
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and direction != 2:
                direction = 0
            elif event.key == pygame.K_DOWN and direction != 3:
                direction = 1
            elif event.key == pygame.K_LEFT and direction != 0:
                direction = 2
            elif event.key == pygame.K_UP and direction != 1:
                direction = 3
            elif event.key == pygame.K_SPACE and not alive:
                alive = True
                snake = [start_pos]
                apple = random.randint(0, borders[0] - 1), random.randint(0, borders[1] - 1)
                fps = 5


    for x, y in snake:
        # Проверка, является ли текущая позиция головой
        if (x, y) == snake[0]:
            # Рисование головы красного цвета
             pygame.draw.rect(screen, (0, 128, 0), (x * snake_size, y * snake_size, snake_size - 1, snake_size - 1))
        else:
            # Рисование остальных сегментов зеленым цветом
            pygame.draw.rect(screen, green, (x * snake_size, y * snake_size, snake_size - 1, snake_size - 1))
        pygame.draw.rect(screen, red, (apple[0] * snake_size, apple[1] * snake_size, snake_size - 1, snake_size - 1))

    new_pos = (
        (snake[0][0] + directions[direction][0]) % borders[0],  # * speedSnake,
        (snake[0][1] + directions[direction][1]) % borders[1] # * speedSnake,
    )

    if alive:
        snake.insert(0, new_pos)
        if new_pos == apple:
            fps += 1 and not fps >= 15
            apple = random.randint(0, borders[0]-1), random.randint(0, borders[1]-1)
        else:
            snake.pop(-1)
        tail = snake[1:]

    if new_pos in tail:
        alive = False
        text = font_gameover.render(f"GAME OVER", True, "white")
        screen.blit(text, (winSize[0] // 2 - text.get_width() // 2, winSize[1] // 2 - 50))
        text = font_space.render(f"Press SPACE for restart", True, "white")
        screen.blit(text, (winSize[0] // 2 - text.get_width() // 2, winSize[1] // 2 + 10))

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
