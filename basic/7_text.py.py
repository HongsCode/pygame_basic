#pip install pygame
import pygame

#pygame 초기화
pygame.init()

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Game")

#FPS
clock = pygame.time.Clock()
#배경, 캐릭터 이미지 불러오기 (회사)
background = pygame.image.load("C:\\Users\\User\\Desktop\\Visual Studio Code Workspace\\python_project\\pygame_basic\\background.png")
#background = pygame.image.load("C:/Users/User/Desktop/Visual Studio Code Workspace/python_project/pygame_basic/background.png")
character = pygame.image.load("C:\\Users\\User\\Desktop\\Visual Studio Code Workspace\\python_project\\pygame_basic\\character.png")

# 집
#background = pygame.image.load("C:\\Users\\Hong\\Desktop\\git\\pygame_basic\\background.png")
#character = pygame.image.load("C:\\Users\\Hong\\Desktop\\git\\pygame_basic\\character.png")

character_size = character.get_rect().size
character_width = character_size[0] # 캐릭터의 가로크기 
character_height= character_size[1] # 캐릭터의 세로크기
character_x_pos = screen_width / 2 - (character_width  / 2) #화면 가로 크기 절반에 위치
character_y_pos = screen_height - character_height

#이동속도
character_speed = 0.6

# 적 캐릭터
enemy = pygame.image.load("C:\\Users\\User\\Desktop\\Visual Studio Code Workspace\\python_project\\pygame_basic\\enemy.png")


enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0] # 캐릭터의 가로크기 
enemy_height= enemy_size[1] # 캐릭터의 세로크기
enemy_x_pos = screen_width / 2 - (enemy_width  / 2) #화면 가로 크기 절반에 위치
enemy_y_pos = (screen_height/2) - (enemy_height/2)


#폰트 정의
game_font = pygame.font.Font(None, 40) #폰트 객체 생성(폰트(None는 Default), 크기)

#총 시간
total_time = 10

#시작 시간 정보
start_ticks = pygame.time.get_ticks() #시간 tick을 받아옴

#이벤트 루프
running = True # 게임이 진행중인가 확인 
to_x = to_y = 0 #캐릭터가 움직일 좌표값
while running:
    dt = clock.tick(30) #게임화면의 초당 Frame 설정

    # 캐릭터가 1초 동안 100만큼 이동해야함
    # 10 fps : 1초동안 10번 동작 -> 1번에 10만큼 이동 10 * 10 = 100
    # 20 fps : 1초동안 20번 동작 -> 1번에 20만큼 이동 20 * 5 = 100
    # Frame에 따라서 게임속도는 차이가 없어야함
    print("fps : " + str(clock.get_fps()))
    for event in pygame.event.get(): #어떤 Event가 발생하였는가
        #사용자의 입력 체크(키보드, 마우스)
        print(event)
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는지 체크
            running = False #Game Running False
        
        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
                    
    # Frame별로 바뀌는 값을 보정하기 위해 dt를 곱함
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > (screen_width - character_width):
        character_x_pos = screen_width - character_width
    
    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height


    #충돌처리를 위한 rect 정보 업데이트, 좌표 실시간 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌체크

    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False


    
    screen.blit(background, (0, 0)) # 배경 불러오기, 배경 좌표 설정
    screen.blit(character, (character_x_pos, character_y_pos )) #캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) #적 그리기
    
    #타이머 집어 넣기
    #경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 
    #경과 시간을 1000으로 나누어서 초 단위로 표시 

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    #render를 이용해서 그리자 
    #시간, True, 글자색상(튜플을 이용해 RGB)

    screen.blit(timer, (10, 10))

    if (total_time - elapsed_time) <= 0:
        print("타임 아웃")
        running = False


    pygame.display.update() # 화면을 매번 그리도록 설정

# 끝내기 전에 잠시 대기 
pygame.time.delay(2000) # 2초 정도 대기
pygame.quit()


