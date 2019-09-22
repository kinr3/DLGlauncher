import os
import time
import socket
import pickle
import threading
import os.path
import string
import pygame
import pygame.locals as pl
from pygame.locals import *


def decode(data):
    letters = string.ascii_letters + string.digits + string.punctuation
    decode_str = ''
    data_n = data.split('#')
    data = []
    for data_z in data_n[:-1]:
        data.append(float(data_z))
    i = 0
    for data_z in data:
        ascii_ = data_z * 2
        decode_str += letters[int(ascii_)]
        i += 1
    decode_str = decode_str.replace('-ou-', 'u')
    decode_str = decode_str.split('#@-@-@#')
    return decode_str


def encode(data):
    letters = string.ascii_letters + string.digits + string.punctuation
    encode_str = ''
    data = str(data)
    data = data.replace('u', '-ou-')
    data = data.replace(' ', '#@-@-@#')
    len_ = data.__len__()
    for data_st in range(len_):
        i = -1
        while data[data_st] != letters[i]:
            i += 1
            if data[data_st] == letters[i]:
                encode_str += str(i / 2) + '#'
        data_st += 1
    return encode_str


def test_len(inp, text_input):
    if inp >= 40:
        text_input.mode['s_l_a'] = False

    else:
        text_input.mode['s_l_a'] = True


def submit():
    global t
    loading_ = True
    # test input
    if checkbox:
        #file = open('data.txt', 'wb')
        #file.write(str(encode(Mail)))
        #file.close()
        pass
    if Mail != '' and PASS_l != '':
        if '@' in Mail:
            if time.time() - t >= 0.3:
                t = time.time()
                try:
                    if c_data.log_in((Mail, PASS_l))['data']:
                        loading_ = False
                except Exception as e:
                    print(e)

    else:
        pass
    return loading_
    # data bas


def submit_reg():
    global t
    loading = True
    # test input
    if checkbox_usk.mode and checkbox_agb.mode:
        if Mail1 != '' and Name1 != '' and Name2 != '' and PASS != '':
            if '@' in Mail1:
                if time.time() - t >= 0.3:
                    t = time.time()
                    loading = False
                    name = Name1 + '_' + Name2
                    mail = Mail1
                    pwd = PASS
                    c_data.new_acc((name, mail, pwd))

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
        screen_1.fill((0, 0, 0))
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
        screen_1.blit(text_name1.get_surface(), text_name_pos1)
        screen_1.blit(text_name2.get_surface(), text_name_pos2)
        screen_1.blit(text_mail1.get_surface(), text_mail_pos1)
        text.show(pdw[:text_pass1.get_cursor_position()], text_pass1_pos, (200, 200, 200), 35)
        if error:
            text.show('***INSUFFICIENT DATA OR WRONG DATA***', (dpa.pro_to_pix((38, 65))), (200, 5, 5), 25)
        if not load:
            if time.time() - t > 0.005:
                t = time.time()
                i += dpa.pro_to_pix((0, 5))[1]
            pygame.draw.rect(screen_1, (255, 255, 255), (0, size[1] - 10, i, 10))
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
                    Mail = text_mail.get_text()
                    PASS_l = text_name.get_text()
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
        screen_1.fill((0, 0, 0))
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
        screen_1.blit(text_mail.get_surface(), text_mail_pos)
        text.show(pdw[:text_name.get_cursor_position()], text_name_pos, (200, 200, 200), 35)
        if error:
            text.show('***INSUFFICIENT DATA OR WRONG DATA***', (dpa.pro_to_pix((32.19, 38.19))), (200, 5, 5), 25)
        if not load:
            if time.time() - t > 0.005:
                t = time.time()
                i += dpa.pro_to_pix((0, 5))[1]
            pygame.draw.rect(screen_1, (255, 255, 255), (0, size[1] - 10, i, 10))
            if i == dpa.pro_to_pix((0, 200))[1]:
                launcher_true = False
        '# Mouse'
        mouse_.show_m(mouse, mouse_clikl)
        '# update'
        pygame.display.flip()
        fps.tick(FPS)


# pygame.draw.rect(screen,(200,0,0),(dpa.pro_to_pix((60.16, 85.00)), (dpa.pro_to_pix((11, 3)))))


def start_loding(ts):
    pygame.init()
    pygame.font.init()
    display_width_ = 500
    display_height_ = 500
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    screen_ = pygame.display.set_mode((display_width_, display_height_), HWSURFACE | DOUBLEBUF | NOFRAME | NOEVENT)
    t_ = time.time()

    '---------------FPS-----------------'
    fps_ = pygame.time.Clock()
    '---------------text---------------'
    text_ = Text(screen_)

    '---DynamicPositionAssignment--dpa--'
    dpa_ = DynamicPositionAssignment(screen_, (display_width_, display_height_))
    dpa_.set_relation((display_width_, display_height_))

    '---------------bg-----------------'
    bg_ = Background(screen_, 'LogoLauncher1.png', dpa_)
    fps_min = 400
    resize_ = []
    i = 0
    txt = 'STARTING'
    start_true = True
    t1 = time.time()
    while start_true:
        pygame.display.set_caption("Launcher. FPS: %.2f" % (fps_.get_fps()))
        for event in pygame.event.get():
            if event.type == 2:
                pass
            if event.type == 6:
                start_true = False
            if event.type == 12:
                start_true = False
            elif event.type == VIDEORESIZE:
                dpa_.set_relation(event.dict['size'])
                for re in resize_:
                    re.resize()
        '---------print------------'
        '#Bg'
        screen_.fill((138, 138, 138))
        bg_.show((display_width_, display_height_), 0)
        if time.time() - t_ > ts:
            start_true = False
        if time.time() - t1 >= ts / 490:
            t1 = time.time()
            i += 1
        pygame.draw.rect(screen_, (255, 255, 255), (0, 490, i, 10))
        '#txt'
        if not time.time() - t_ > ts * 0.1:
            txt = 'CHECKING FOR UPDATES.'
        elif not time.time() - t_ > ts * 0.2:
            txt = 'CHECKING FOR UPDATES..'
        elif not time.time() - t_ > ts * 0.3:
            txt = 'CHECKING FOR UPDATES...'
        elif not time.time() - t_ > ts * 0.4:
            txt = 'CHECKING FOR UPDATES.'
        elif not time.time() - t_ > ts * 0.5:
            txt = 'CHECKING FOR UPDATES..'
        elif not time.time() - t_ > ts * 0.6:
            txt = 'CHECKING FOR UPDATES...'
        elif not time.time() - t_ > ts * 0.62:
            txt = 'CHECKING FOR UPDATES.'
        elif not time.time() - t_ > ts * 0.7:
            txt = 'CHECKING FOR UPDATES COMPLETED'
        elif not time.time() - t_ > ts * 0.85:
            txt = 'STARTING LAUNCHER.'
        elif not time.time() - t_ > ts * 0.89:
            txt = 'STARTING LAUNCHER..'
        elif not time.time() - t_ > ts * 0.9:
            txt = 'STARTING LAUNCHER...'
        text_.show(txt, (5, 470), (255, 255, 255), 22)
        '# Mouse'
        pygame.display.flip()
        fps_.tick(fps_min)
    return True


class Connection:
    def __init__(self):
        self.HEADERSIZE = 253
        self.HOST = '127.0.0.1'
        self.PORT = 62914
        self.msg = None
        self.online = 'online'
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.connect((self.HOST, self.PORT))
        except Exception as e:
            self.online = str(e)
        thread = threading.Thread(target=self.get_msg)
        thread.daemon = True
        thread.start()

    def send(self, msg):
        msg = pickle.dumps(msg)
        msg = bytes(f"{len(msg):<{self.HEADERSIZE}}", 'utf-8') + msg
        self.s.send(msg)

    def get_msg(self):
        try:
            while True:
                full_msg = b''
                new_msg = True
                msglen = None
                while True:
                    msg = self.s.recv(16)
                    if new_msg:
                        msglen = int(msg[:self.HEADERSIZE])
                        new_msg = False
                    full_msg += msg
                    if len(full_msg) - self.HEADERSIZE == msglen:
                        self.msg = pickle.loads(full_msg[self.HEADERSIZE:])
                        new_msg = True
                        full_msg = b""
                        self.handler()
        except Exception as e_:
            print(e_, 'no')
            pass

    def handler(self):
        pass

    def test_version(self, v):
        data = {'version': v}
        self.send(data)

    def log_in(self, data):
        mail, pwd = data
        mail = encode(mail)
        pwd = encode(pwd)
        self.send(msg={'info': 'log_in', 'data': [{'data': mail}, {'data': pwd}]})
        time.sleep(2)
        return self.msg

    def new_acc(self, data):
        name, mail, pwd = data
        mail = encode(mail)
        pwd = encode(pwd)
        name = encode(name)
        self.send(msg={'info': 'new_acc', 'data': [{'data': mail}, {'data': pwd},
                                                   {'data': name}]})


class Background:

    def __init__(self, screen, image_n, dpa_):
        img = pygame.image.load('image/' + str(image_n)).convert_alpha()
        self.screen = screen
        self.Bglist = [img]
        self.Bglist_ = [image_n]
        self.i = 0
        self.dpa = dpa_

    def add_bg(self, image_n):
        img = pygame.image.load('image/' + str(image_n)).convert_alpha()
        self.Bglist.append(img)
        self.Bglist_.append(image_n)

    def remove_bg(self, image_n):
        img = pygame.image.load('image/' + str(image_n)).convert_alpha()
        self.Bglist.remove(img)
        self.Bglist_.remove(image_n)

    def get_list(self):
        return self.Bglist_

    def show(self, size, num=0):
        img = pygame.transform.scale(self.Bglist[num], size)
        self.screen.blit(img, (0, 0))


class DynamicPositionAssignment:
    def __init__(self, screen, size):
        self.screen = screen
        w = size[0] / 100
        h = size[1] / 100
        self.relation = {'pxW': w,
                         'pxH': h}

    def pro_to_pix(self, wh):
        pix_w = wh[0] * self.relation['pxW']
        pix_h = wh[1] * self.relation['pxH']
        return pix_w, pix_h

    def pix_to_pro(self, wh):
        pro_w = wh[0] / self.relation['pxW']
        pro_h = wh[1] / self.relation['pxH']
        return pro_w, pro_h

    def rect_to_pro(self, rect):
        pw = 0
        ph = 0
        try:
            pw = rect[2] - rect[0]
            ph = rect[3] - rect[1]
            pw = pw / self.relation['pxW']
            ph = ph / self.relation['pxH']
        except ZeroDivisionError as z:
            z += '1'
            pass
        return pw, ph

    def set_relation(self, size):
        w = size[0] / 100
        h = size[1] / 100
        self.relation = {'pxW': w,
                         'pxH': h}

    def assignment(self, wh):
        return int(wh[0] * self.relation['pxW']), int(wh[1] * self.relation['pxH'])

    def assignment_img(self, img, wh):
        return pygame.transform.scale(img, self.assignment(wh))

    def set_img_to_pro(self, img, pro):
        return pygame.transform.scale(img, (int(pro[0] * self.relation['pxW']), int(pro[1] * self.relation['pxH'])))


class Text:

    def __init__(self, screen):
        self.screen = screen

    def show(self, text_, xy, color_=(0, 0, 0), size=30, text_type='Arial.ttf'):
        self.screen.blit(pygame.font.SysFont(text_type, size)
                         .render(str(text_), False, color_), xy)


class Objects:

    def __init__(self):
        self.mode = {'color': (255, 255, 255), 's_l_a': False,
                     'py': False, 'wh': (0, 0), 'pro': (0, 0), 'p_on_p_pro': (0, 0), 'p_on_p': (0, 0),
                     'on_hit': False, 'object': None}

    def set_all(self, color_=(255, 255, 255), py=False, sla=False, wh=(0, 0), p_on_p=(0, 0), obj=None, pro=(0, 0),
                p_on_p_pro=(0, 0)):
        self.mode['color'] = color_
        self.mode['py'] = py
        self.mode['s_l_a'] = sla
        self.mode['wh'] = wh
        self.mode['p_on_p'] = p_on_p
        self.mode['object'] = obj
        self.mode['pro'] = pro
        self.mode['p_on_p_pro'] = p_on_p_pro

    def set_color(self, color_):
        self.mode['color'] = color_

    def set_py(self, py):
        self.mode['py'] = py

    def set_sla(self, sla):
        self.mode['s_l_a'] = sla

    def set_wh(self, wh):
        self.mode['wh'] = wh

    def set_ponp(self, p_on_p):
        self.mode['p_on_p'] = p_on_p

    def set_pro(self, pro):
        self.mode['pro'] = pro

    def set_ponp_pro(self, p_on_p_pro):
        self.mode['p_on_p_pro'] = p_on_p_pro

    def set_obj(self, objects):
        self.mode['object'] = objects

    def test_on_hit_l(self, x, y):
        if self.mode['p_on_p'][0] + self.mode['wh'][0] >= x >= self.mode['p_on_p'][1] \
                and self.mode['p_on_p'][0] + self.mode['wh'][1] >= y >= self.mode['p_on_p'][1] \
                and self.mode['p_on_p'][0] + self.mode['wh'][0] >= y <= self.mode['p_on_p'][1] + self.mode['wh'][1] \
                and self.mode['p_on_p'][0] <= x >= self.mode['p_on_p'][1]:
            self.mode['on_hit'] = True
        else:
            self.mode['on_hit'] = False
        return self.mode['on_hit']

    def load(self):
        return self.mode

    def g_rect(self):
        return pygame.Rect(self.mode['p_on_p'][0], self.mode['p_on_p'][1], self.mode['wh'][0], self.mode['wh'][1])


class Collision:

    def __init__(self):
        self.collision_ = False
        self.list1 = []

    def set_fix(self, ob2):
        ob2.mode = ob2.load()
        list1 = []
        for i in range(ob2.mode['wh'][0] + 1):
            x = i + ob2.mode['p_on_p'][0]

            for i1 in range(ob2.mode['wh'][1] + 1):
                y = i1 + ob2.mode['p_on_p'][1]
                list1.append((x, y))

        self.list1 = list1

    def collision_f(self, ob1):
        i2 = 0
        ob1.mode = ob1.load()
        while i2 != self.list1.__len__():
            a = self.list1[i2]
            i2 += 1
            if ob1.test_on_hit_l(a[0], a[1]):
                return True, a
            else:
                pass
        return False, None

    @staticmethod
    def collision(ob1, ob2):
        ob1.mode = ob1.load()
        ob2.mode = ob2.load()
        ob2.list = []
        a = 0
        for i in range(ob2.mode['wh'][0] + 1):
            x = i + ob2.mode['p_on_p'][0]
            if i == 0 or i == ob2.mode['wh'][0]:
                a = 1

            for i1 in range(ob2.mode['wh'][1] + 1):
                y = i1 + ob2.mode['p_on_p'][1]
                if a == 1:
                    ob2.list.append((x, y))
                    a = 0
                elif i1 == 0 or i1 == ob2.mode['wh'][1]:
                    ob2.list.append((x, y))
                    a = 0
        i2 = 0
        while i2 != ob2.list.__len__():
            a = ob2.list[i2]
            i2 += 1
            if ob1.test_on_hit_l(a[0], a[1]):
                return True, a
            else:
                pass
        return False, None

    @staticmethod
    def coll_rect(ob1, ob2):
        rect1 = ob1.g_rect()
        rect2 = ob2.g_rect()
        return rect1.colliderect(rect2)

    @staticmethod
    def coll_self(ob1, rect2):
        rect1 = ob1.g_rect()
        return rect1.colliderect(rect2)

    @staticmethod
    def coll_s_rect(rect1, rect2):
        return rect1.colliderect(rect2)


class Mouse:

    def __init__(self, img_s, screen):
        mouse = pygame.transform.scale(pygame.image.load('image/' + str(img_s[0])).convert_alpha(), (20, 20))
        mouse1 = pygame.transform.scale(pygame.image.load('image/' + str(img_s[1])).convert_alpha(), (20, 20))
        self.mouse = mouse, mouse1
        self.screen = screen
        pygame.mouse.set_visible(False)

    def mouse_get_rect(self, mouse):
        return self.mouse[0].get_rect().move(mouse)

    def show_m(self, mouse, click):
        if click:
            pass
            self.screen.blit(self.mouse[1], mouse)
        else:
            pass
            self.screen.blit(self.mouse[0], mouse)


class TextBox(Objects, Collision, Text):

    def __init__(self, screen, names, point, wh, dpa_):
        Objects.__init__(self)
        Collision.__init__(self)
        self.screen = screen
        self.dpa = dpa_
        self.pwh = dpa_.pro_to_pix(wh)
        self.p_point = dpa_.pro_to_pix(point)
        self.set_all(wh=self.pwh, p_on_p=self.p_point, pro=wh, p_on_p_pro=point)
        self.img = self.dpa.set_img_to_pro(pygame.image.load('image/' + str(names[0])).convert_alpha(), wh)
        self.img1 = self.dpa.set_img_to_pro(pygame.image.load('image/' + str(names[1])).convert_alpha(), wh)


class Image:

    def __init__(self, screen, name, pos, wh, dpa_):
        self.pos = pos
        self.b_pos = dpa_.pro_to_pix(pos)
        self.wh = wh
        self.dpa = dpa_
        self.screen = screen
        self.name = name
        self.img = pygame.image.load('image/' + str(name)).convert_alpha()

    def show(self):
        img = self.dpa.set_img_to_pro(self.img, self.wh)
        self.screen.blit(img, self.dpa.pro_to_pix(self.pos))


class Button(Objects, Collision):

    def __init__(self, screen, names, point, wh, dpa_):
        Objects.__init__(self)
        Collision.__init__(self)
        self.screen = screen
        self.dpa = dpa_
        self.pwh = dpa_.pro_to_pix(wh)
        self.p_point = dpa_.pro_to_pix(point)
        self.set_all(wh=self.pwh, p_on_p=self.p_point, pro=wh, p_on_p_pro=point)
        self.img = self.dpa.set_img_to_pro(pygame.image.load('image/' + str(names[0])).convert_alpha(), wh)
        self.img1 = self.dpa.set_img_to_pro(pygame.image.load('image/' + str(names[1])).convert_alpha(), wh)

    def resize(self):
        self.pwh = self.dpa.pro_to_pix(self.mode['pro'])
        self.p_point = self.dpa.pro_to_pix(self.mode['p_on_p_pro'])
        self.set_wh(self.pwh)
        self.set_ponp(self.p_point)

    def show(self, m_rect, click):
        img = self.dpa.set_img_to_pro(self.img, self.mode['pro'])
        self.screen.blit(img, self.dpa.pro_to_pix(self.mode['p_on_p_pro']))
        if self.coll_self(self, m_rect):
            img1 = self.dpa.set_img_to_pro(self.img1, self.mode['pro'])
            self.screen.blit(img1, self.dpa.pro_to_pix(self.mode['p_on_p_pro']))
        if click == 1:
            return self.coll_self(self, m_rect)
        else:
            return False


class TextInput:
    def __init__(
            self,
            initial_string="",
            font_family="",
            font_size=30,
            antialias=True,
            text_color=(200, 200, 200),
            cursor_color=(255, 255, 255),
            repeat_keys_initial_ms=400,
            repeat_keys_interval_ms=35):
        # Text related vars:
        self.antialias = antialias
        self.text_color = text_color
        self.font_size = font_size
        self.input_string = initial_string  # Inputted text

        if not os.path.isfile(font_family):
            font_family = pygame.font.match_font(font_family)

        self.font_object = pygame.font.Font(font_family, font_size)

        # Text-surface will be created during the first update call:
        self.surface = pygame.Surface((1, 1))
        self.surface.set_alpha(0)

        # Vars to make keydowns repeat after user pressed a key for some time:
        self.keyrepeat_counters = {}  # {event.key: (counter_int, event.unicode)} (look for "***")
        self.keyrepeat_intial_interval_ms = repeat_keys_initial_ms
        self.keyrepeat_interval_ms = repeat_keys_interval_ms

        # Things cursor:
        self.cursor_surface = pygame.Surface((int(self.font_size / 20 + 1), self.font_size))
        self.cursor_surface.fill(cursor_color)
        self.cursor_position = len(initial_string)  # Inside text
        self.cursor_visible = True  # Switches every self.cursor_switch_ms ms
        self.cursor_switch_ms = 500  # /|\
        self.cursor_ms_counter = 0

        self.clock = pygame.time.Clock()

    def max_list(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.cursor_visible = True  # So the user sees where he writes

                # If none exist, create counter for that key:
                if event.key not in self.keyrepeat_counters:
                    self.keyrepeat_counters[event.key] = [0, event.unicode]

                if event.key == pl.K_BACKSPACE:
                    self.input_string = (
                            self.input_string[:max(self.cursor_position - 1, 0)]
                            + self.input_string[self.cursor_position:]
                    )

                    # Subtract one from cursor_pos, but do not go below zero:
                    self.cursor_position = max(self.cursor_position - 1, 0)
                elif event.key == pl.K_DELETE:
                    self.input_string = (
                            self.input_string[:self.cursor_position]
                            + self.input_string[self.cursor_position + 1:]
                    )

                elif event.key == pl.K_RETURN:
                    return True

                elif event.key == pl.K_RIGHT:
                    # Add one to cursor_pos, but do not exceed len(input_string)
                    self.cursor_position = min(self.cursor_position + 1, len(self.input_string))

                elif event.key == pl.K_LEFT:
                    # Subtract one from cursor_pos, but do not go below zero:
                    self.cursor_position = max(self.cursor_position - 1, 0)

                elif event.key == pl.K_END:
                    self.cursor_position = len(self.input_string)

                elif event.key == pl.K_HOME:
                    self.cursor_position = 0

                else:
                    self.cursor_position += len(event.unicode)  # Some are empty, e.g. K_UP

            elif event.type == pl.KEYUP:
                # *** Because KEYUP doesn't include event.unicode, this dict is stored in such a weird way
                if event.key in self.keyrepeat_counters:
                    del self.keyrepeat_counters[event.key]

        # Update key counters:
        for key in self.keyrepeat_counters:
            self.keyrepeat_counters[key][0] += self.clock.get_time()  # Update clock

            # Generate new key events if enough time has passed:
            if self.keyrepeat_counters[key][0] >= self.keyrepeat_intial_interval_ms:
                self.keyrepeat_counters[key][0] = (
                        self.keyrepeat_intial_interval_ms
                        - self.keyrepeat_interval_ms
                )

                event_key, event_unicode = key, self.keyrepeat_counters[key][1]
                pygame.event.post(pygame.event.Event(pl.KEYDOWN, key=event_key, unicode=event_unicode))

        # Re-render text surface:
        self.surface = self.font_object.render(self.input_string, self.antialias, self.text_color)

        # Update self.cursor_visible
        self.cursor_ms_counter += self.clock.get_time()
        if self.cursor_ms_counter >= self.cursor_switch_ms:
            self.cursor_ms_counter %= self.cursor_switch_ms
            self.cursor_visible = not self.cursor_visible

        if self.cursor_visible:
            cursor_y_pos = self.font_object.size(self.input_string[:self.cursor_position])[0]
            # Without this, the cursor is invisible when self.cursor_position > 0:
            if self.cursor_position > 0:
                cursor_y_pos -= self.cursor_surface.get_width()
            self.surface.blit(self.cursor_surface, (cursor_y_pos, 0))

        self.clock.tick()
        return False

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.cursor_visible = True  # So the user sees where he writes

                # If none exist, create counter for that key:
                if event.key not in self.keyrepeat_counters:
                    self.keyrepeat_counters[event.key] = [0, event.unicode]

                if event.key == pl.K_BACKSPACE:
                    self.input_string = (
                            self.input_string[:max(self.cursor_position - 1, 0)]
                            + self.input_string[self.cursor_position:]
                    )

                    # Subtract one from cursor_pos, but do not go below zero:
                    self.cursor_position = max(self.cursor_position - 1, 0)
                elif event.key == pl.K_DELETE:
                    self.input_string = (
                            self.input_string[:self.cursor_position]
                            + self.input_string[self.cursor_position + 1:]
                    )

                elif event.key == pl.K_RETURN:
                    return True

                elif event.key == pl.K_RIGHT:
                    # Add one to cursor_pos, but do not exceed len(input_string)
                    self.cursor_position = min(self.cursor_position + 1, len(self.input_string))

                elif event.key == pl.K_LEFT:
                    # Subtract one from cursor_pos, but do not go below zero:
                    self.cursor_position = max(self.cursor_position - 1, 0)

                elif event.key == pl.K_END:
                    self.cursor_position = len(self.input_string)

                elif event.key == pl.K_HOME:
                    self.cursor_position = 0

                else:
                    # If no special key is pressed, add unicode of key to input_string
                    self.input_string = (
                            self.input_string[:self.cursor_position]
                            + event.unicode
                            + self.input_string[self.cursor_position:]
                    )
                    self.cursor_position += len(event.unicode)  # Some are empty, e.g. K_UP

            elif event.type == pl.KEYUP:
                # *** Because KEYUP doesn't include event.unicode, this dict is stored in such a weird way
                if event.key in self.keyrepeat_counters:
                    del self.keyrepeat_counters[event.key]

        # Update key counters:
        for key in self.keyrepeat_counters:
            self.keyrepeat_counters[key][0] += self.clock.get_time()  # Update clock

            # Generate new key events if enough time has passed:
            if self.keyrepeat_counters[key][0] >= self.keyrepeat_intial_interval_ms:
                self.keyrepeat_counters[key][0] = (
                        self.keyrepeat_intial_interval_ms
                        - self.keyrepeat_interval_ms
                )

                event_key, event_unicode = key, self.keyrepeat_counters[key][1]
                pygame.event.post(pygame.event.Event(pl.KEYDOWN, key=event_key, unicode=event_unicode))

        # Re-render text surface:
        self.surface = self.font_object.render(self.input_string, self.antialias, self.text_color)

        # Update self.cursor_visible
        self.cursor_ms_counter += self.clock.get_time()
        if self.cursor_ms_counter >= self.cursor_switch_ms:
            self.cursor_ms_counter %= self.cursor_switch_ms
            self.cursor_visible = not self.cursor_visible

        if self.cursor_visible:
            cursor_y_pos = self.font_object.size(self.input_string[:self.cursor_position])[0]
            # Without this, the cursor is invisible when self.cursor_position > 0:
            if self.cursor_position > 0:
                cursor_y_pos -= self.cursor_surface.get_width()
            self.surface.blit(self.cursor_surface, (cursor_y_pos, 0))

        self.clock.tick()
        return False

    def get_surface(self):
        return self.surface

    def get_text(self):
        return self.input_string

    def get_cursor_position(self):
        return self.cursor_position

    def set_text_color(self, color_):
        self.text_color = color_

    def set_cursor_color(self, color_):
        self.cursor_surface.fill(color_)

    def clear_text(self):
        self.input_string = ""
        self.cursor_position = 0


if __name__ == '__main__':
    os.system('CD')
    ver = 0
    c_data = Connection()
    try:
        c_data.test_version(ver)
    except OSError as os_error:
        print(os_error)
        time.sleep(2)
    t = 2
    tim = time.time()
    while not c_data.msg:
        print('starting in t: ' + str((time.time() - tim) - 10)[:2])
        os.system('cls')
        if time.time() - tim - 10 >= 0:
            print('starting offline ')
            time.sleep(1)
            break
    try:
        if not c_data.msg['had']:
            print('update')
            t = 20
            file = open('lau.zip', 'ab')
            file.write(c_data.msg['zip'])
            file.close()
    except Exception as e:
        print('connection error', e)

    start_loding(t)
    try:
        file = open('data.txt', 'rb')
        file_data = decode(pickle.loads(file.read()))
        file.close()
        file1 = open('data.txt', 'wb')
        file1.write(pickle.dumps(encode(file_data)))
        file1.close()
    except Exception as en:
        file_data = ''
        print(en)
    if c_data.online != 'online':
        c_data.online = 'offline'
    online = c_data.online[:16]
    pygame.init()
    pygame.font.init()
    display_width = 1280
    display_height = 720
    screen_1 = pygame.display.set_mode((display_width, display_height), HWSURFACE | DOUBLEBUF, 32)
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.display.set_caption('launcher')
    os.system('cls')
    '---------------FPS-----------------'
    fps = pygame.time.Clock()
    FPS = 20

    '---DynamicPositionAssignment--dpa--'
    dpa = DynamicPositionAssignment(screen_1, (display_width, display_height))
    dpa.set_relation((display_width, display_height))

    '--------obj------------------------'
    '-----------root--------------------'
    checkbox = Objects()
    checkbox.set_all(p_on_p=dpa.pro_to_pix((30.00, 57.78)), wh=(dpa.pro_to_pix((2.29, 4.4))))
    image_checkbox = Image(screen_1, 'Haken.png', (28.4, 54.8), (6, 10.6), dpa)

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
    image_checkbox_agb = Image(screen_1, 'Haken.png', (69, 51.25), (6, 10.6), dpa)

    checkbox_usk = Objects()
    checkbox_usk.set_all(p_on_p=dpa.pro_to_pix((29.77, 55.28)), wh=(dpa.pro_to_pix((1.5, 3.05))))
    image_checkbox_usk = Image(screen_1, 'Haken.png', (27.6, 51.25), (6, 10.6), dpa)

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
    mouse_ = Mouse(['Mauszeiger.png', 'Mauszeiger.png'], screen_1)

    '-------------text------------------'
    text = Text(screen_1)

    '---------------bg-----------------'
    bg = Background(screen_1, 'LoginFenster.png', dpa)
    bg.add_bg('Register.png')
    '------------Resize----------------'
    resize = []

    '------------Button----------------'

    '---------------Bid----------------'

    '-------------text_input------------'
    '-------------log_in----------------'
    text_mail = TextInput(initial_string=file_data)
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
    try:
        launcher()
    except Exception as e:
        print('system error or offline')
        launcher()
    pygame.quit()
