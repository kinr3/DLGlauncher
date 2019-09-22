import pygame
import os
import time
import sys
import time
from Objects import *
from text_input import *
from pygame.locals import *
from py_lau_scripts.client import Connection
pygame.init()
pygame.font.init()
display_width = 1280
display_height = 720
screen = pygame.display.set_mode((display_width, display_height), HWSURFACE | DOUBLEBUF, 32)
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.display.set_caption('launcher')
os.system('cls')
'---------------FPS-----------------'
fps = pygame.time.Clock()
FPS = 20

'---DynamicPositionAssignment--dpa--'
dpa = DynamicPositionAssignment(screen, (display_width, display_height))
dpa.set_relation((display_width, display_height))

'--------obj------------------------'
'-----------root--------------------'
checkbox = Objects()
checkbox.set_all(p_on_p=dpa.pro_to_pix((30.00, 57.78)), wh=(dpa.pro_to_pix((2.29, 4.4))))
image_checkbox = Image(screen, 'Haken.png', (28.4, 54.8), (6, 10.6), dpa)

exit_ = Objects()
exit_.set_all(p_on_p=dpa.pro_to_pix((95, 0)), wh=(dpa.pro_to_pix((5, 5))))

Mail_ = Objects()
Mail_.set_all(sla=True, p_on_p=dpa.pro_to_pix((29.84, 29.03)), wh=(dpa.pro_to_pix((40.16, 7.08))))

Name_ = Objects()
Name_.set_all(sla=True, p_on_p=dpa.pro_to_pix((30.00, 44.44)), wh=(dpa.pro_to_pix((40.16, 7.08))))

Www_ = Objects()
Www_.set_all(sla=True, p_on_p=dpa.pro_to_pix((2, 3.4)), wh=(dpa.pro_to_pix((6.95, 12.80))))

Submit_ = Objects()
Submit_.set_all(sla=True, p_on_p=dpa.pro_to_pix((38.98, 71.53)), wh=(dpa.pro_to_pix((20.24, 7.36))))

Register_ = Objects()
Register_.set_all(sla=True, p_on_p=dpa.pro_to_pix((60.16, 85.00)), wh=(dpa.pro_to_pix((11, 3))))

Forgot_Password_ = Objects()
Forgot_Password_.set_all(sla=True, p_on_p=dpa.pro_to_pix((56.02, 58.61)), wh=(dpa.pro_to_pix((13.82, 3.33))))

Privacy_Policy_ = Objects()
Privacy_Policy_.set_all(sla=True, p_on_p=dpa.pro_to_pix((45.3125, 90.27)), wh=(dpa.pro_to_pix((8.75, 2.36))))

'--------------register-------------'
checkbox_agb = Objects()
checkbox_agb.set_all(p_on_p=dpa.pro_to_pix((71.2, 55.28)), wh=(dpa.pro_to_pix((1.5, 3.05))))
image_checkbox_agb = Image(screen, 'Haken.png', (69, 51.25), (6, 10.6), dpa)

checkbox_usk = Objects()
checkbox_usk.set_all(p_on_p=dpa.pro_to_pix((29.77, 55.28)), wh=(dpa.pro_to_pix((1.5, 3.05))))
image_checkbox_usk = Image(screen, 'Haken.png', (27.6, 51.25), (6, 10.6), dpa)

Login_ = Objects()
Login_.set_all(sla=True, p_on_p=dpa.pro_to_pix((61.48, 80.97)), wh=(dpa.pro_to_pix((7, 3))))

Privacy_Policy1_ = Objects()
Privacy_Policy1_.set_all(sla=True, p_on_p=dpa.pro_to_pix((47.81, 86.11)), wh=(dpa.pro_to_pix((6.09, 2.22))))

Mail1_ = Objects()
Mail1_.set_all(sla=True, p_on_p=dpa.pro_to_pix((29.69, 34.31)), wh=(dpa.pro_to_pix((42.97, 7.08))))

Name1_ = Objects()
Name1_.set_all(sla=True, p_on_p=dpa.pro_to_pix((29.53, 21.94)), wh=(dpa.pro_to_pix((20.31, 7.36))))

Name2_ = Objects()
Name2_.set_all(sla=True, p_on_p=dpa.pro_to_pix((52.50, 21.81)), wh=(dpa.pro_to_pix((20.23, 7.50))))

Password1_ = Objects()
Password1_.set_all(sla=True, p_on_p=dpa.pro_to_pix((40.62, 45.28)), wh=(dpa.pro_to_pix((20.31, 7.50))))

Submit_reg_ = Objects()
Submit_reg_.set_all(sla=True, p_on_p=dpa.pro_to_pix((44.06, 71.11)), wh=(dpa.pro_to_pix((13.59, 5.42))))
'---------------mouse---------------'
mouse_ = Mouse(['Mauszeiger.png', 'Mauszeiger.png'], screen)

'-------------text------------------'
text = Text(screen)

'---------------bg-----------------'
bg = Background(screen, 'LoginFenster.png', dpa)
bg.add_bg('Register.png')
'------------Resize----------------'
resize = []

'------------Button----------------'

'---------------Bid----------------'

'-------------text_input------------'
'-------------log_in----------------'
text_mail = TextInput()
text_mail_pos = (dpa.pro_to_pix((30.23, 32.92)))
text_name = TextInput(cursor_color=(0, 0, 0))
text_name_pos = (dpa.pro_to_pix((30.23, 48.7)))

'---------------register--------------'
text_mail1 = TextInput()
text_mail_pos1 = (dpa.pro_to_pix((30.69, 38.31)))
text_name1 = TextInput()
text_name_pos1 = (dpa.pro_to_pix((30.53, 25.94)))
text_name2 = TextInput()
text_name_pos2 = (dpa.pro_to_pix((53.50, 25.81)))
text_pass1 = TextInput(cursor_color=(255, 255, 255))
text_pass1_pos = (dpa.pro_to_pix((41.62, 49.68)))


def test_len(inp, text_input):
    if inp >= 40:
        text_input.mode['s_l_a'] = False

    else:
        text_input.mode['s_l_a'] = True


def submit():
    global t
    loading_ = True
    # test input
    if Mail != '' and PASS_l != '':
        if '@' in Mail:
            if time.time() - t >= 0.3:
                t = time.time()
                print(Mail, '##')
                loading_ = False
                print(data.log_in(Mail1, PASS_l))

    else:
        pass
    return loading_
    # data bas


def submit_reg():
    global t
    loading = True
    # test input
    if Mail1 != '' and Name1 != '' and Name2 != '' and PASS != '':
        if '@' in Mail1:
            if time.time() - t >= 0.3:
                t = time.time()
                print(Mail1, Name1, Name2)
                loading = False
                name = Name1+'_'+Name2
                mail = Mail1
                pwd = PASS
                print(data.new_acc(name, mail, pwd))

    else:
        pass

    return loading
    # data bas


def register():
    global Mail1, Name1, Name2, PASS, t
    t = time.time()
    i = 0
    Mail1 = ''
    Name1 = ''
    Name2 = ''
    PASS = ''
    load = submit_reg()
    pdw = '*************************************'
    register_true = True
    error = False
    size = (display_width, display_height)
    # strt = (0, 0)
    # xy = (1, 1)
    # strt_ = True
    while register_true:
        mouse = pygame.mouse.get_pos()
        mouse_clikl = pygame.mouse.get_pressed()[0]
        # mouse_clikr = pygame.mouse.get_pressed()[2]
        pygame.display.set_caption("Launcher. FPS: %.2f" % (fps.get_fps()))
        '#mouse = pygame.mouse.get_pos()'
        events = pygame.event.get()
        for event in events:
            '#print(event, event.type)'
            if event.type == 6:
                # if strt_:  # red bpx
                #     strt_ = False  # red bpx
                #     strt = dpa.pix_to_pro(mouse)  # red bpx
                # else:  # red bpx
                #     xy = dpa.pix_to_pro(mouse)[0] - strt[0], dpa.pix_to_pro(mouse)[1] - strt[1]  # red bpx
                #     print('.set_all(sla=True, p_on_p=dpa.pro_to_pix((%.2f, %.2f)),' % strt,  # red bpx
                #           'wh=(dpa.pro_to_pix((%.2f, %.2f))))' % xy)  # red bpx
                # print(mouse, '##%.2f, %.2f' % dpa.pix_to_pro(mouse))
                if checkbox_usk.g_rect().colliderect(mouse_.mouse_get_rect(mouse)):
                    if checkbox_usk.mode['py']:
                        checkbox_usk.mode['py'] = False
                    else:
                        checkbox_usk.mode['py'] = True
                if checkbox_agb.g_rect().colliderect(mouse_.mouse_get_rect(mouse)):
                    if checkbox_agb.mode['py']:
                        checkbox_agb.mode['py'] = False
                    else:
                        checkbox_agb.mode['py'] = True
                if Name1_.g_rect().colliderect(mouse_.mouse_get_rect(mouse)):
                    if Name1_.mode['py']:
                        Name1_.mode['py'] = False
                    else:
                        Name1_.mode['py'] = True
                        Password1_.mode['py'] = False
                        Mail1_.mode['py'] = False
                        Name2_.mode['py'] = False
                if Name2_.g_rect().colliderect(mouse_.mouse_get_rect(mouse)):
                    if Name2_.mode['py']:
                        Name2_.mode['py'] = False
                    else:
                        Name2_.mode['py'] = True
                        Password1_.mode['py'] = False
                        Mail1_.mode['py'] = False
                        Name1_.mode['py'] = False
                if Mail1_.g_rect().colliderect(mouse_.mouse_get_rect(mouse)):
                    if Mail1_.mode['py']:
                        Mail1_.mode['py'] = False
                    else:
                        Mail1_.mode['py'] = True
                        Password1_.mode['py'] = False
                        Name2_.mode['py'] = False
                        Name1_.mode['py'] = False
                if Password1_.g_rect().colliderect(mouse_.mouse_get_rect(mouse)):
                    if Password1_.mode['py']:
                        Password1_.mode['py'] = False
                    else:
                        Password1_.mode['py'] = True
                        Mail1_.mode['py'] = False
                        Name2_.mode['py'] = False
                        Name1_.mode['py'] = False
                if Www_.g_rect().colliderect(mouse_.mouse_get_rect(mouse)):
                    os.system('start http://dreamlifegames.com/')
                if Submit_reg_.g_rect().colliderect(mouse_.mouse_get_rect(mouse)):
                    Mail1 = text_mail1.get_text()
                    Name1 = text_name1.get_text()
                    Name2 = text_name2.get_text()
                    PASS = text_pass1.get_text()
                    error = submit_reg()
                    load = error
                if Login_.g_rect().colliderect(mouse_.mouse_get_rect(mouse)):
                    register_true = False
                    text_name1.clear_text()
                    text_mail1.clear_text()
                    text_name2.clear_text()
                    text_pass1.clear_text()
                    launcher()
                if Privacy_Policy_.g_rect().colliderect(mouse_.mouse_get_rect(mouse)):
                    os.system('start http://dreamlifegames.com/')
                if exit_.g_rect().colliderect(mouse_.mouse_get_rect(mouse)):
                    register_true = False
            if event.type == 2:
                pass
            if event.type == 12:
                '#exit'
                register_true = False
            elif event.type == VIDEORESIZE:
                size = event.dict['size']
                dpa.set_relation(event.dict['size'])
                for re in resize:
                    re.resize()
        '---------print------------'
        '#Bg'
        screen.fill((0, 0, 0))
        bg.show(size, 1)
        '# text'
        text.show(online, (1100, 10), (255, 255, 255), 25)
        # pygame.draw.rect(screen, (200, 0, 0), (dpa.pro_to_pix(strt), (dpa.pro_to_pix((xy))))) # red bpx
        '#checkbox'
        if checkbox_usk.mode['py']:
            image_checkbox_usk.show()
        if checkbox_agb.mode['py']:
            image_checkbox_agb.show()
        '#textInput'
        test_len(text_mail1.get_cursor_position(), Mail1_)
        test_len(text_name1.get_cursor_position(), Name1_)
        test_len(text_name2.get_cursor_position(), Name2_)
        test_len(text_pass1.get_cursor_position(), Password1_)
        if Name1_.mode['s_l_a']:
            if Name1_.mode['py']:
                text_mail1.cursor_visible = False
                text_name2.cursor_visible = False
                text_pass1.cursor_visible = False
                if text_name1.update(events):
                    Name1 = text_name1.get_text()
        else:
            if text_name.max_list(events):
                Name1 = text_name.get_text()
        if Name2_.mode['s_l_a']:
            text_name2.cursor_visible = True
            if Name2_.mode['py']:
                Name2 = text_name2.get_text()
                text_name2.update(events)
        else:
            text_name2.cursor_visible = False
            text_name2.max_list(events)
        if Mail1_.mode['s_l_a']:
            text_mail1.cursor_visible = True
            if Mail1_.mode['py']:
                text_mail1.update(events)
        else:
            text_mail1.cursor_visible = False
            text_mail1.max_list(events)
        if Password1_.mode['s_l_a']:
            text_pass1.cursor_visible = True
            if Password1_.mode['py']:
                text_pass1.update(events)
        else:
            text_pass1.cursor_visible = False
            text_pass1.max_list(events)

        '#text box'
        screen.blit(text_name1.get_surface(), text_name_pos1)
        screen.blit(text_name2.get_surface(), text_name_pos2)
        screen.blit(text_mail1.get_surface(), text_mail_pos1)
        text.show(pdw[:text_pass1.get_cursor_position()], text_pass1_pos, (200, 200, 200), 35)
        if error:
            text.show('***INSUFFICIENT DATA OR WRONG DATA***', (dpa.pro_to_pix((38, 65))), (200, 5, 5), 25)
        if not load:
            if time.time() - t > 0.005:
                t = time.time()
                i += dpa.pro_to_pix((0, 5))[1]
            pygame.draw.rect(screen, (255, 255, 255), (0, size[1] - 10, i, 10))
            if i == dpa.pro_to_pix((0, 200))[1]:
                register_true = False
                launcher()
        '# Mouse'
        mouse_.show_m(mouse, mouse_clikl)
        '# update'
        pygame.display.flip()
        fps.tick(FPS)


def launcher():
    global Mail, PASS_l, online, t
    t = time.time()
    i = 0
    Mail = ''
    PASS_l = ''
    load = submit()
    pdw = '***************************'
    launcher_true = True
    error = False
    size = (display_width, display_height)
    # strt = (0, 0)
    # xy = (1, 1)
    # strt_ = True
    while launcher_true:
        mouse = pygame.mouse.get_pos()
        mouse_clikl = pygame.mouse.get_pressed()[0]
        # mouse_clikr = pygame.mouse.get_pressed()[2]
        pygame.display.set_caption("Launcher. FPS: %.2f" % (fps.get_fps()))
        '#mouse = pygame.mouse.get_pos()'
        events = pygame.event.get()
        for event in events:
            '#print(event, event.type)'
            if event.type == 6:
                # if strt_:
                #     strt_ = False
                #     strt = dpa.pix_to_pro(mouse)
                # else:
                #     xy = dpa.pix_to_pro(mouse)[0] - strt[0], dpa.pix_to_pro(mouse)[1] - strt[1]
                #     print('.set_all(sla=True, p_on_p=dpa.pro_to_pix((%.2f, %.2f)),' % strt,
                #           'wh=(dpa.pro_to_pix((%.2f, %.2f))))' % xy)
                # print(mouse, '##%.2f, %.2f' % dpa.pix_to_pro(mouse))
                if checkbox.g_rect().colliderect(mouse_.mouse_get_rect(mouse)):
                    if checkbox.mode['py']:
                        checkbox.mode['py'] = False
                    else:
                        checkbox.mode['py'] = True
                if Mail_.g_rect().colliderect(mouse_.mouse_get_rect(mouse)):
                    if Mail_.mode['py']:
                        Mail_.mode['py'] = False
                    else:
                        Mail_.mode['py'] = True
                        Name_.mode['py'] = False
                if Name_.g_rect().colliderect(mouse_.mouse_get_rect(mouse)):
                    if Name_.mode['py']:
                        Name_.mode['py'] = False
                    else:
                        Name_.mode['py'] = True
                        Mail_.mode['py'] = False
                if Www_.g_rect().colliderect(mouse_.mouse_get_rect(mouse)):
                    os.system('start http://dreamlifegames.com/')
                if Submit_.g_rect().colliderect(mouse_.mouse_get_rect(mouse)):
                    error = submit()
                    load = error
                if Register_.g_rect().colliderect(mouse_.mouse_get_rect(mouse)):
                    launcher_true = False
                    text_name.clear_text()
                    text_mail.clear_text()
                    register()
                if exit_.g_rect().colliderect(mouse_.mouse_get_rect(mouse)):
                    launcher_true = False
                if Forgot_Password_.g_rect().colliderect(mouse_.mouse_get_rect(mouse)):
                    print('XD')
                if Privacy_Policy_.g_rect().colliderect(mouse_.mouse_get_rect(mouse)):
                    os.system('start http://dreamlifegames.com/')
            if event.type == 2:
                pass
            if event.type == 12:
                '#exit'
                launcher_true = False
            elif event.type == VIDEORESIZE:
                size = event.dict['size']
                dpa.set_relation(event.dict['size'])
                for re in resize:
                    re.resize()
        '---------print------------'
        '#Bg'
        screen.fill((0, 0, 0))
        bg.show(size)
        '# text'
        text.show(online, (1100, 10), (255, 255, 255), 25)
        # pygame.draw.rect(screen, (200, 0, 0), (dpa.pro_to_pix(strt), (dpa.pro_to_pix((xy))))) # hit
        '#checkbox'
        if checkbox.mode['py']:
            image_checkbox.show()
        '#textInput'
        test_len(text_mail.get_cursor_position(), Mail_)
        test_len(text_name.get_cursor_position(), Name_)
        if Name_.mode['s_l_a']:
            if Name_.mode['py']:
                text_mail.cursor_visible = False
                if text_name.update(events):
                    Mail = text_mail.get_text()
                    PASS_l = text_name.get_text()
                    error = submit()
                    load = submit()
        else:
            if text_name.max_list(events):
                Mail = text_mail.get_text()
                PASS_l = text_name.get_text()
                error = submit()
                load = submit()
        if Mail_.mode['s_l_a']:
            text_mail.cursor_visible = True
            if Mail_.mode['py']:
                Mail = text_mail.get_text()
                text_mail.update(events)
        else:
            text_mail.cursor_visible = False
            text_mail.max_list(events)

        '#text box'
        screen.blit(text_mail.get_surface(), text_mail_pos)
        text.show(pdw[:text_name.get_cursor_position()], text_name_pos, (200, 200, 200), 35)
        if error:
            text.show('***INSUFFICIENT DATA OR WRONG DATA***', (dpa.pro_to_pix((32.19, 38.19))), (200, 5, 5), 25)
        if not load:
            if time.time() - t > 0.005:
                t = time.time()
                i += dpa.pro_to_pix((0, 5))[1]
            pygame.draw.rect(screen, (255, 255, 255), (0, size[1]-10, i, 10))
            if i == dpa.pro_to_pix((0, 200))[1]:
                launcher_true = False
        '# Mouse'
        mouse_.show_m(mouse, mouse_clikl)
        '# update'
        pygame.display.flip()
        fps.tick(FPS)
# pygame.draw.rect(screen,(200,0,0),(dpa.pro_to_pix((60.16, 85.00)), (dpa.pro_to_pix((11, 3)))))


if __name__ == '__main__':
    os.system('CD')
    time.sleep(11)
    ver = 1
    c_data = Connection()
    try:
        c_data.test_version(ver)
    except OSError as os_error:
        pass
    t = 2
    tim = time.time()
    while not c_data.msg:
        print('starting in t-: ' + str(time.time() - tim))
        os.system('cls')
        if time.time() - tim > 10:
            pass

    if not c_data.msg['had']:
        print('updata')
        t = 20
        file = open('lau.zip', 'ab')
        file.write(c_data.msg['zip'])
        file.close()
    os.system("python start.py " + str(t))
    online = c_data.online
    launcher()
    pygame.quit()
    sys.exit()
