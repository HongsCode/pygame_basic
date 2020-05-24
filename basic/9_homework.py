import pygame
import random

pygame.init()

screen_width = 480
screen_height = 640

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Avoid Game")

clock = pygame.time.Clock()


background = pygame.image.load("C:\\Users\\User\\Desktop\\Visual Studio Code Workspace\\python_project\\pygame_basic\\background.png")
character = pygame.image.load("C:\\Users\\User\\Desktop\\Visual Studio Code Workspace\\python_project\\pygame_basic\\character.png")
enemy = pygame.image.load("C:\\Users\\User\\Desktop\\Visual Studio Code Workspace\\python_project\\pygame_basic\\enemy.png")
missile = pygame.image.load("C:\\Users\\User\\Desktop\\Visual Studio Code Workspace\\python_project\\pygame_basic\\missile.png")

#character, enemy의 크기 및 초기 위치
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width-1)
enemy_y_pos = 0

missile_size = missile.get_rect().size
missile_width = missile_size[0]
missile_height = missile_size[1]

missile_x_pos = character_x_pos + (character_width / 2) - (missile_width/2)
missile_y_pos = character_y_pos - (missile_height)



running = True
character_speed = 0.3
enemy_speed = 0.3
to_x = to_y = 0
while running:
    dt = clock.tick(30)
    
    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. 캐릭터, 적군 위치
    character_x_pos += (to_x * dt)
    if character_x_pos < 0:
        character_x_pos = 0
    if character_x_pos > (screen_width - character_width):
        character_x_pos = (screen_width - character_width)

    if missile_y_pos < 0:
        missile_x_pos = character_x_pos + (character_width / 2) - (missile_width/2)
        missile_y_pos = character_y_pos - (missile_height)
        to_y = 0

    # 미사일 위치
    if to_y == 0:
        missile_x_pos = character_x_pos + (character_width / 2) - (missile_width/2)
        missile_y_pos = character_y_pos - (missile_height)
    else:
        missile_y_pos += (to_y * dt)

    # 현재 character 위치, enemy 위치 확인
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    missile_rect = missile.get_rect()
    missile_rect.left = missile_x_pos
    missile_rect.top = missile_y_pos

    # 4. 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    if missile_rect.colliderect(enemy_rect):
        print("맞추다")
        running = False

    if enemy_y_pos >= screen_height:
        enemy_x_pos = random.randint(0, screen_width - enemy_width-1)
        enemy_y_pos = 0

    # 5. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    screen.blit(missile, (missile_x_pos, missile_y_pos))
    enemy_y_pos += (enemy_speed *dt)
    pygame.display.update()

pygame.quit()