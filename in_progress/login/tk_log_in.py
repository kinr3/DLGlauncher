import tkinter as tk
from tkinter import ttk as ttk
import os
import webbrowser
import string
import time
import socket
import pickle
import threading


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


class Connection:
    def __init__(self):
        self.HEADERSIZE = 10
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
        data = {'version': v, 'info': None}
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

    @staticmethod
    def data_dic(data):
        return {'info': data[0], 'version': data[4], 'data': [{'data': data[1]},
                                                              {'data': data[2]},
                                                              {'data': data[3]}, ]}


class Handler(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        HEIGHT = 720
        WIDTH = 1280
        image_init()
        self.iconbitmap(default=r'image/elements/LogoLauncher1.ico')
        container = tk.Frame(self, height=HEIGHT, width=WIDTH,
                             highlightbackground="black", highlightcolor="black", highlightthickness=25,  bd=0)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.title('')

        self.frames = {}

        for F in frames_list:

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(FrameOne)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class FrameOne(tk.Frame):

    def __init__(self, parent, cotroller):
        self.cotroller = cotroller
        tk.Frame.__init__(self, parent)
        self.configure(background="black")
        self.tbx_name_v = tk.StringVar(self, value=g_mail())
        self.tbx_pass_v = tk.StringVar(self, value='')
        self.name_v = tk.StringVar(self, value='E-MAIL:')
        self.pass_v = tk.StringVar(self, value='PASSWORD:')
        self.DreamLifeGames = ttk.Label(self, text="                    DreamLifeGames                    ",
                                        font=S_LARGE_FONT, background='black', foreground='white')
        self.ico = ttk.Label(self, image=image['DLG_Ico.png'], background='black')
        self.text_EMAI = ttk.Label(self, textvariable=self.name_v, background='black', foreground='white',
                                   font=LARGE_FONT)
        self.text_PASSWORD = ttk.Label(self, textvariable=self.pass_v, background='black', foreground='white',
                                       font=LARGE_FONT)
        self.text_ANMELDEN = ttk.Label(self, text='                    ANMELDEN                    ',
                                       background='black', foreground='white', font=LARGE_FONT)

        self.button_img_pass = tk.Button(self, image=image['DLG_Pass_v.png'], background='black',
                                           command=self.pass_button, border=0)
        self.button_img_submit = tk.Button(self, image=image['DLG_Anmelden.png'], background='black',
                                           command=self.submit_button, border=0)
        self.button_img_police = tk.Button(self, image=image['DLG_Privacy_Policey.png'], background='black',
                                           command=self.police_button, border=0)
        self.button_img_register = tk.Button(self, image=image['DLG_Registrieren.png'], background='black',
                                             command=self.register_button, border=0)

        self.tbx_name = tk.Entry(self, textvariable=self.tbx_name_v, width=40, font=TBX_FONT,
                                 background='black', foreground='white')
        self.tbx_pass = tk.Entry(self, textvariable=self.tbx_pass_v, width=40, font=TBX_FONT,
                                 background='black', foreground='white', show="*")
        self.ico.grid(row=0, column=0, sticky='w')
        self.DreamLifeGames.grid(row=0, column=1, sticky='ns')
        self.text_ANMELDEN.grid(row=1, column=1, sticky='ns')
        self.text_EMAI.grid(row=2, column=1, sticky='w', pady=25)
        self.tbx_name.grid(row=2, column=1)
        self.text_PASSWORD.grid(row=4, column=1, sticky='w', pady=35)
        self.tbx_pass.grid(row=4, column=1)
        self.button_img_pass.grid(row=7, column=1)
        self.button_img_submit.grid(row=8, column=1, pady=15)
        self.button_img_register.grid(row=9, column=1, pady=15)
        self.button_img_police.grid(row=10, column=1, pady=5)


    @staticmethod
    def pass_button():
        webbrowser.open('http://dreamlifegames.com/', new=1)

    @staticmethod
    def police_button():
        webbrowser.open('https://dreamlifegames.com/contact.php', new=1)

    def submit_button(self):
        if self.tbx_name_v.get() != '' and self.tbx_pass_v.get() != '':
            if '@' in self.tbx_name_v.get():
                try:
                    if c_data.log_in((self.tbx_name_v.get(), self.tbx_pass_v.get()))['data']:
                        s_mail(self.tbx_name_v.get())
                        self.cotroller.show_frame(FrameTwo)
                    print(c_data.log_in((self.tbx_name_v.get(), self.tbx_pass_v.get()))['data'], '~#~')
                except Exception as e:
                    self.name_v.set('E-MAIL: -X-')
                    self.pass_v.set('PASSWORD: -X-')
                    print(e)
            else:
                self.name_v.set('E-MAIL: ?-@-?')
        else:
            self.name_v.set('E-MAIL: empty')
            self.pass_v.set('PASSWORD: empty')
            pass

    def register_button(self):
        self.cotroller.show_frame(FrameThee)


class FrameTwo(tk.Frame):

    def __init__(self, parent, cotroller):
        tk.Frame.__init__(self, parent)
        button_switsch = ttk.Button(self, image=image['DLG_DatenMerken0.png'],
                                    command=lambda: cotroller.show_frame(FrameOne)).pack()

        pass


class FrameThee(tk.Frame):

    def __init__(self, parent, cotroller):
        self.cotroller = cotroller
        tk.Frame.__init__(self, parent)
        self.configure(background="black")
        self.tbx_name1_v = tk.StringVar(self, value='')
        self.tbx_name2_v = tk.StringVar(self, value='')
        self.tbx_name_v = tk.StringVar(self, value='')
        self.tbx_pass_v = tk.StringVar(self, value='')
        self.name_v = tk.StringVar(self, value='E-MAIL:')
        self.pass_v = tk.StringVar(self, value='PASSWORD:')
        self.age_button_v = 0
        self.agb_button_v = 0

        self.DreamLifeGames = ttk.Label(self, text="                    DreamLifeGames                    ",
                                        font=S_LARGE_FONT, background='black', foreground='white')
        self.ico = ttk.Label(self, image=image['DLG_Ico.png'], background='black')
        self.text_EMAI = ttk.Label(self, textvariable=self.name_v, background='black', foreground='white',
                                   font=LARGE_FONT)
        self.text_NAME1 = ttk.Label(self, text='Name:', background='black', foreground='white',
                                   font=LARGE_FONT)
        self.text_NAME2 = ttk.Label(self, text='NachName:', background='black', foreground='white',
                                   font=LARGE_FONT)
        self.text_PASSWORD = ttk.Label(self, textvariable=self.pass_v, background='black', foreground='white',
                                       font=LARGE_FONT)
        self.text_REGISTER = ttk.Label(self, text='                    REGISTER                    ',
                                       background='black', foreground='white', font=LARGE_FONT)

        self.button_img_submit = tk.Button(self, image=image['DLG_Register_submit.png'], background='black',
                                           command=self.register_button, border=0)
        self.button_img_police = tk.Button(self, image=image['DLG_Privacy_Policey.png'], background='black',
                                           command=self.police_button, border=0)

        self.tbx_name1 = tk.Entry(self, textvariable=self.tbx_name1_v, width=20, font=TBX_FONT,
                                 background='black', foreground='white')
        self.tbx_name2 = tk.Entry(self, textvariable=self.tbx_name2_v, width=20, font=TBX_FONT,
                                 background='black', foreground='white')
        self.tbx_mail = tk.Entry(self, textvariable=self.tbx_name_v, width=40, font=TBX_FONT,
                                 background='black', foreground='white')
        self.tbx_pass = tk.Entry(self, textvariable=self.tbx_pass_v, width=40, font=TBX_FONT,
                                 background='black', foreground='white', show="*")

        self.button_img_agb_box = tk.Button(self, image=image['DLG_Register_agb.png'], background='black',
                                         command=self.agb_button, border=0)
        self.button_img_age_box = tk.Button(self, image=image['DLG_Register_16.png'], background='black',
                                         command=self.age_button, border=0)
        self.button_log_in = tk.Button(self, image=image['DLG_Register_back.png'], background='black',
                                         command=self.back_button, border=0)

        self.ico.grid(row=0, column=0, sticky='w')
        self.DreamLifeGames.grid(row=0, column=1, sticky='ns')
        self.text_REGISTER.grid(row=1, column=1, sticky='ns', pady=5)
        self.text_NAME1.grid(row=2, column=1, sticky='w', pady=10)
        self.text_NAME2.grid(row=3, column=1, sticky='w', pady=10)
        self.tbx_name1.grid(row=2, column=1)
        self.tbx_name2.grid(row=3, column=1)
        self.text_EMAI.grid(row=5, column=1, sticky='w', pady=20)
        self.tbx_mail.grid(row=5, column=1)
        self.text_PASSWORD.grid(row=6, column=1, sticky='w', pady=25)
        self.tbx_pass.grid(row=6, column=1)
        self.button_img_agb_box.grid(row=7, column=1, pady=5)
        self.button_img_age_box.grid(row=7, column=1, sticky='w', pady=5)
        self.button_img_submit.grid(row=8, column=1, pady=15)
        self.button_log_in.grid(row=9, column=1)
        self.button_img_police.grid(row=10, column=1, pady=5)

        #button_switsch = ttk.Button(self, text='starting L',
        #                            command=lambda: cotroller.show_frame(FrameOne))

    @staticmethod
    def police_button():
        print('pw')
        webbrowser.open('https://dreamlifegames.com/contact.php', new=1)

    def register_button(self):
        # test input
        pass
        if self.age_button_v == 1 and self.agb_button_v == 1:
            if self.tbx_name_v.get() != '' and self.tbx_name1_v.get() != '' and self.tbx_name2_v.get() != '' and \
                    self.tbx_pass_v.get() != '':
                if '@' in self.tbx_name_v.get():
                        name = self.tbx_name1_v.get() + '_' + self.tbx_name2_v.get()
                        mail = self.tbx_name_v.get()
                        pwd = self.tbx_pass_v.get()
                        c_data.new_acc((name, mail, pwd))
                        self.cotroller.show_frame(FrameOne)
                else:
                    self.name_v.set('E-MAIL: -X-')
        self.name_v.set('E-MAIL: agb, age ?')

    def agb_button(self):
        if self.agb_button_v == 0:
            self.agb_button_v = 1
            self.button_img_agb_box['image'] = image['DLG_Register_agb_1.png']
        else:
            self.agb_button_v = 0
            self.button_img_agb_box['image'] = image['DLG_Register_agb.png']
        pass

    def age_button(self):
        if self.age_button_v == 0:
            self.age_button_v = 1
            self.button_img_age_box['image'] = image['DLG_Register_16_1.png']
        else:
            self.age_button_v = 0
            self.button_img_age_box['image'] = image['DLG_Register_16.png']
        pass

    def back_button(self):
        self.cotroller.show_frame(FrameOne)


class FrameZero(tk.Frame):

    def __init__(self, parent, cotroller):
        tk.Frame.__init__(self, parent)
        self.cotroller = cotroller
        self.var = tk.StringVar()
        self.var.set('CHECKING FOR UPDATES.')

        label = ttk.Label(self, image=image['LogoLauncher1.png'], background='black')
        label.grid(row=0, column=0, sticky='w')

        self.label1 = ttk.Label(self, textvariable=self.var, background='black', foreground='white', font=LARGE_FONT)
        self.label1.grid(row=1, column=0, sticky='we')

        self.progress = ttk.Progressbar(self, orient=tk.HORIZONTAL, length=120)
        self.progress.grid(row=2, column=0, sticky='we')
        self.progress.config(mode='determinate', maximum=219)
        self.progress.step(5)
        self.progress.start()
        cThread = threading.Thread(target=self.first_concat)
        cThread.daemon = True
        cThread.start()

    def first_concat(self):
        i = 0
        a = 0.1
        if a:
            try:
                c_data.test_version(ver)
                self.var.set('ONLINE START NO UPDATES')
                i = 60
            except OSError as os_error:
                self.var.set('OFFLINE START')
                print(os_error)
                a = 0.15
        time.sleep(0.75)
        while i <= 100:
            time.sleep(a)
            if c_data.msg:
                self.var.set('ONLINE START')
            else:
                self.var.set('OFFLINE START')
            if i >= 2:
                self.var.set('CHECKING FOR UPDATES.')
            if i >= 10:
                self.var.set('CHECKING FOR UPDATES..')
            if i >= 15:
                self.var.set('CHECKING FOR UPDATES...')
            if i >= 30:
                self.var.set('CHECKING FOR UPDATES.')
            if i >= 45:
                self.var.set('CHECKING FOR UPDATES..')
            if i >= 60:
                self.var.set('CHECKING FOR UPDATES COMPLETED')
            if i >= 75:
                self.var.set('STARTING LAUNCHER.')
            if i >= 80:
                self.var.set('STARTING LAUNCHER..')
            if i >= 90:
                self.var.set('STARTING LAUNCHER...')
            self.update_idletasks()
            i += 1
        self.progress.stop()
        try:
            if not c_data.msg['had']:
                self.var.set('UPDATE')
                file = open('lau.zip', 'ab')
                file.write(c_data.msg['zip'])
                file.close()
        except Exception as e:
            print('connection error', e)
        time.sleep(1.5)
        self.cotroller.show_frame(FrameOne)


def image_init():
    global image
    image['LogoLauncher1.png'] = tk.PhotoImage(file="image/elements/LogoLauncher1.png")
    image['DLG_Ico.png'] = tk.PhotoImage(file="image/elements/DLG_Ico.png")
    image['DLG_DatenMerken0.png'] = tk.PhotoImage(file="image/elements/DLG_DatenMerken0.png")
    image['DLG_DatenMerken1.png'] = tk.PhotoImage(file="image/elements/DLG_DatenMerken1.png")
    image['DLG_Pass_v.png'] = tk.PhotoImage(file="image/elements/DLG_Pass_v.png")
    image['DLG_Anmelden.png'] = tk.PhotoImage(file="image/elements/DLG_Anmelden.png")
    image['DLG_Privacy_Policey.png'] = tk.PhotoImage(file="image/elements/DLG_Privacy_Policey.png")
    image['DLG_Registrieren.png'] = tk.PhotoImage(file="image/elements/DLG_Registrieren.png")
    image['DLG_Register_submit.png'] = tk.PhotoImage(file="image/elements/DLG_Register_submit.png")
    image['DLG_Register_back.png'] = tk.PhotoImage(file="image/elements/DLG_Register_back.png")
    image['DLG_Register_16.png'] = tk.PhotoImage(file="image/elements/DLG_Register_16.png")
    image['DLG_Register_16_1.png'] = tk.PhotoImage(file="image/elements/DLG_Register_16_1.png")
    image['DLG_Register_agb.png'] = tk.PhotoImage(file="image/elements/DLG_Register_agb.png")
    image['DLG_Register_agb_1.png'] = tk.PhotoImage(file="image/elements/DLG_Register_agb_1.png")


def init_font():
    global LARGE_FONT, S_LARGE_FONT, TBX_FONT
    LARGE_FONT = ("Arial", 12)
    S_LARGE_FONT = ("Arial", 30)
    TBX_FONT = ("Arial", 14)


def g_mail():
    try:
        data = open('data~@run', 'rb')
        mail = str(data.read(), 'utf-8')
        mail = decode(mail)
    except Exception as e:
        print(e)
        data = open('data~@run', 'ab')
        mail = ''
    data.close()
    return mail


def s_mail(mail):
    try:
        data = open('data~@run', 'wb')
        data.write(bytes(encode(mail), 'utf-8'))
    except Exception as e:
        print(e)
        data = open('data~@run', 'ab')
    data.close()


if __name__ == "__main__":
    frames_list = (FrameOne, FrameZero, FrameTwo, FrameThee)
    init_font()
    c_data = Connection()
    ver = 0
    image = {}
    app = Handler()
    app.mainloop()

