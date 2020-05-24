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

#이벤트 루프

running = True # 게임이 진행중인가 확인 

while running:
    for event in pygame.event.get(): #어떤 Event가 발생하였는가
        #사용자의 입력 체크(키보드, 마우스)
        print(event)
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는지 체크
            running = False #Game Running False


pygame.quit()

