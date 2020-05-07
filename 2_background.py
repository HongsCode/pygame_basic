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
#이벤트 루프
running = True # 게임이 진행중인가 확인 

while running:
    for event in pygame.event.get(): #어떤 Event가 발생하였는가
        #사용자의 입력 체크(키보드, 마우스)
        print(event)
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는지 체크
            running = False #Game Running False
    #screen.fill((255, 0, 0)) #화면 배경 채우기, fill로 RGB로 줄수도 있음
    screen.blit(background, (0, 0)) # 배경 불러오기, 배경 좌표 설정

    pygame.display.update() # 화면을 매번 그리도록 설정

pygame.quit()

