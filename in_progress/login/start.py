from Objects import *
import pygame
import os
import sys
import time
from pygame.locals import *
ts = int(sys.argv[1])
pygame.init()
pygame.font.init()
display_width = 500
display_height = 500
os.environ["SDL_VIDEO_CENTERED"] = "1"
screen = pygame.display.set_mode((display_width, display_height), HWSURFACE | DOUBLEBUF | NOFRAME | NOEVENT)
t = time.time()

'---------------FPS-----------------'
fps = pygame.time.Clock()
FPS = 400
'---------------text---------------'
text = Text(screen)

'---DynamicPositionAssignment--dpa--'
dpa = DynamicPositionAssignment(screen, (display_width, display_height))
dpa.set_relation((display_width, display_height))

'---------------bg-----------------'
bg = Background(screen, 'LogoLauncher1.png', dpa)

'------------Resize----------------'
resize = []


def start():
    i = 0
    txt = 'STARTING'
    start_true = True
    t1 = time.time()
    while start_true:
        pygame.display.set_caption("Launcher. FPS: %.2f" % (fps.get_fps()))
        for event in pygame.event.get():
            if event.type == 2:
                pass
            if event.type == 6:
                start_true = False
                pygame.quit()
                sys.exit()
            if event.type == 12:
                start_true = False
            elif event.type == VIDEORESIZE:
                dpa.set_relation(event.dict['size'])
                for re in resize:
                    re.resize()
        '---------print------------'
        '#Bg'
        screen.fill((138, 138, 138))
        bg.show((display_width, display_height), 0)
        if time.time() - t > ts:
            start_true = False
            pygame.quit()
            sys.exit()
        if time.time() - t1 >= ts/490:
            t1 = time.time()
            i += 1
        pygame.draw.rect(screen, (255, 255, 255), (0, 490, i, 10))
        '#txt'
        if not time.time() - t > ts*0.1:
            txt = 'CHECKING FOR UPDATES.'
        elif not time.time() - t > ts*0.2:
            txt = 'CHECKING FOR UPDATES..'
        elif not time.time() - t > ts*0.3:
            txt = 'CHECKING FOR UPDATES...'
        elif not time.time() - t > ts*0.4:
            txt = 'CHECKING FOR UPDATES.'
        elif not time.time() - t > ts*0.5:
            txt = 'CHECKING FOR UPDATES..'
        elif not time.time() - t > ts*0.6:
            txt = 'CHECKING FOR UPDATES...'
        elif not time.time() - t > ts*0.62:
            txt = 'CHECKING FOR UPDATES.'
        elif not time.time() - t > ts*0.7:
            txt = 'CHECKING FOR UPDATES COMPLETED'
        elif not time.time() - t > ts*0.85:
            txt = 'STARTING LAUNCHER.'
        elif not time.time() - t > ts*0.89:
            txt = 'STARTING LAUNCHER..'
        elif not time.time() - t > ts*0.9:
            txt = 'STARTING LAUNCHER...'
        text.show(txt, (5, 470), (255, 255, 255), 22)
        '# Mouse'
        pygame.display.flip()
        fps.tick(FPS)


start()
pygame.quit()
sys.exit()
