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

#배경이미지 불러오기
background = pygame.image.load("C:\\Users\\User\\Desktop\\Visual Studio Code Workspace\\python_project\\pygame_basic\\background.png")
#background = pygame.image.load("C:/Users/User/Desktop/Visual Studio Code Workspace/python_project/pygame_basic/background.png")

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load("C:\\Users\\User\\Desktop\\Visual Studio Code Workspace\\python_project\\pygame_basic\\character.png")
character_size = character.get_rect().size
character_width = character_size[0] # 캐릭터의 가로크기 
character_height= character_size[1] # 캐릭터의 세로크기
character_x_pos = screen_width / 2 - (character_width  / 2) #화면 가로 크기 절반에 위치
character_y_pos = screen_height - character_height

print (character_size, character_width, character_height)

#이벤트 루프
running = True # 게임이 진행중인가 확인 

while running:
    for event in pygame.event.get(): #어떤 Event가 발생하였는가
        #사용자의 입력 체크(키보드, 마우스)
        print(event)
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는지 체크
            running = False #Game Running False
        
    screen.blit(background, (0, 0)) # 배경 불러오기, 배경 좌표 설정
    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기
    
    pygame.display.update() # 화면을 매번 그리도록 설정

pygame.quit()


