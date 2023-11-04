#import thư viện
import pygame, random
import sys
pygame.init()

gavity = 0.25   
bird_movement = 0
pipe_list = []

def draw_floor():
    screen.blit(floor,(floor_x,500))
    screen.blit(floor,(floor_x + 580,500))

def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def create_pipe():
    pipe_random_pos = random.choice([300,350,400])
    bottom_pipe = pipe1.get_rect(midtop = (600,pipe_random_pos))
    top_pipe = pipe1.get_rect(midtop = (600,pipe_random_pos-400))
    return bottom_pipe, top_pipe

def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >= 500:
            screen.blit(pipe1,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe1,False,True)
            screen.blit(flip_pipe,pipe)

#Display
width = 500
length = 600
screen = pygame.display.set_mode((width,length))
pygame.display.set_caption("The silly bird =))")

#Assets
bird = pygame.image.load(r'assets\bird.png').convert()
background = pygame.image.load(r'assets\bg.png').convert()
floor = pygame.image.load(r'assets\floor.png').convert()
pipe1 = pygame.image.load(r'assets\pipe-green.png').convert()

#Variable
floor_x = 0
pipe_x = 500

#FPS
clock = pygame.time.Clock()

#Location
bird_surf = bird.get_rect(center = (100,300))

#Timer 
spawn_pipe = pygame.USEREVENT
pygame.time.set_timer(spawn_pipe,1200)


#Loop
while True:
    #event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0 
                bird_movement =- 7   
        if event.type == spawn_pipe:
            pipe_list.extend(create_pipe())
            
    
    bird_movement += gavity
    bird_surf.centery += bird_movement

    #Blit assets
    screen.blit(background,(0,0))
    screen.blit(bird,bird_surf)
    
    #pipe
    pipe_list = move_pipe(pipe_list)
    draw_pipe(pipe_list)
    
    #Position
    floor_x -= 2
    if floor_x <= -580:
        floor_x = 0

   
   #def
    draw_floor()
    #post-production
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
