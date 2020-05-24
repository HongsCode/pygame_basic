#pip install pygame
import pygame
import os

###########################################################

#기본 초기화 (반드시 해야하는 것들)
pygame.init()

#화면 크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado pang")

#FPS
clock = pygame.time.Clock()
##################################################

# 1. 사용자 게임 초기화(배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

#배경, 캐릭터 이미지 불러오기 (회사)
#background = pygame.image.load("C:\\Users\\User\\Desktop\\Visual Studio Code Workspace\\python_project\\pygame_basic\\background.png")
#background = pygame.image.load("C:/Users/User/Desktop/Visual Studio Code Workspace/python_project/pygame_basic/background.png")
#character = pygame.image.load("C:\\Users\\User\\Desktop\\Visual Studio Code Workspace\\python_project\\pygame_basic\\character.png")

current_path = os.path.dirname(__file__) #현재 파일의 위치
image_path = os.path.join(current_path, "images") #이미지 폴더 위치 반환

#배경만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

#스테이지 만들기
stage  = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] #스테이지 높이위에 캐릭터 그리기

#캐릭터 만들기
character = pygame.image.load(os.path.join(image_path,image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0] # 캐릭터의 가로크기 
character_height= character_size[1] # 캐릭터의 세로크기
character_x_pos = screen_width / 2 - (character_width  / 2) #화면 가로 크기 절반에 위치
character_y_pos = screen_height - stage_height - character_height


#이벤트 루프
running = True # 게임이 진행중인가 확인 

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

    
    screen.blit(background, (0, 0)) # 배경 불러오기, 배경 좌표 설정
    screen.blit(stage, (0, screen_height - stage_height)) # 스테이지 그리기
    screen.blit(character, (character_x_pos, character_y_pos )) #캐릭터 그리기
    
    
    pygame.display.update() # 화면을 매번 그리도록 설정

pygame.quit()


