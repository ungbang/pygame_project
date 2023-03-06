import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Ungbang Game")

# 배경이미지 불러오기
background = pygame.image.load("C:/Python/230306 python_game_project/background.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0,0)) # 배경 그리기
    # screen.fill((0,0,255)) # 배경 색 채우기
    pygame.display.update()

pygame.quit()