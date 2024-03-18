# import pygame
# from pygame.locals import *


# pygame.init()
# pygame.font.init()
# w , h = 600, 450
# white = (255, 255, 255)
# red = (255, 0 , 0)
# blue = (0, 0, 255)
# green = (0, 255, 0)



# screen = pygame.display.set_mode((w,h))
# clock = pygame.time.Clock()
# FPS = 60


# clock_size = (300, 225)



# pygame.display.set_caption("Alibek's game!")
# font = pygame.font.SysFont("Courier New", 40)

# class mickeyclock():
#     def __init__(self, clock_size):
#         self.clock_size = clock_size
        
#     def


import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((500, 400))
running = True
is_blue = True


clock = pygame.time.Clock()
main_clock = pygame.image.load("images/clock/mainclock.png")
minute = pygame.image.load(("images/clock/rightarm.png"))
second = pygame.image.load(("images/clock/leftarm.png"))
main_clock = pygame.transform.scale(main_clock, (500, 400))
# minute = pygame.transform.scale(minute, (100, 300))
# second = pygame.transform.scale(second, (100, 300))

while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        exit()
        #         if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        #                 is_blue = not is_blue
        
        # pressed = pygame.key.get_pressed()
        # if pressed[pygame.K_UP]: y -= 3
        # if pressed[pygame.K_DOWN]: y += 3
        # if pressed[pygame.K_LEFT]: x -= 3
        # if pressed[pygame.K_RIGHT]: x += 3
        
        screen.fill((255, 255, 255))
        current_time = datetime.datetime.now()
        intmin = int(current_time.strftime("%M"))

        intsec = int(current_time.strftime("%S"))


        minute_angle = intmin * 6 * -1
        second_angle = intsec * 6 * -1
        # if is_blue: color = (0, 128, 255)
        # else: color = (255, 100, 0)
        # pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
        minute = pygame.transform.rotate(minute, minute_angle)
        second = pygame.transform.rotate(second, second_angle)




        screen.blit(main_clock, main_clock.get_rect(center = screen.get_rect().center))
        screen.blit(minute, minute.get_rect(center = screen.get_rect().center))
        screen.blit(second, second.get_rect(center = screen.get_rect().center))
        pygame.display.flip()
        clock.tick(120)
pygame.quit()

    


