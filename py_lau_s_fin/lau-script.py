import socket
import mysql.connector
import threading
import pickle
import hashlib


class Hashlib:

    @staticmethod
    def start_pass(pwd):
        c = hashlib.sha512()
        pwd = bytes(pwd, 'utf-8')
        c.update(pwd)
        return c.hexdigest()


class DataSQL:
    commands = {'new_acc': 'INSERT INTO launcher.user_acc (id, name, mail, pwd , isadmin) VALUES (%s,%s, %s, %s, %s)',
                'select_all': 'SELECT * FROM use_acc', 'select_name': 'SELECT name FROM user_acc',
                'select_mail': 'SELECT mail FROM launcher.user_acc', 'select_pwd': 'SELECT pwd FROM user_acc',
                'where_name': 'SELECT * FROM user_acc WHERE name = %s',
                'where_mail': 'SELECT * FROM user_acc WHERE mail = %s',
                'where_mail_p': 'SELECT pwd FROM user_acc WHERE mail = %s',
                'where_pwd': 'SELECT * FROM user_acc WHERE pwd = %s',
                'update_pwd_mail': 'UPDATE user_acc SET pwd= %s WHERE mail= %s',
                'update_pwd_name': 'UPDATE user_acc SET pwd= %s WHERE name= %s',
                'update_isadmin': 'UPDATE user_acc SET isadmin = 1 WHERE pwd = %s',
                'get-max(id)': 'SELECT MAX(Id) FROM user_acc'}

    def __init__(self):
        self.data = None
        self.database = mysql.connector.connect(
            host='134.255.217.76',
            user='launcherdb',
            passwd='Rj51tt9?',
            database='launcher'
        )
        self.cursor = self.database.cursor()

    def where(self, i, data):
        # print(i, data, 'Where')
        if data:
            self.cursor.execute(self.commands[i], data)
        else:
            self.cursor.execute(self.commands[i])
        self.data = self.cursor.fetchall()
        return self.data

    def fetchall(self, i, data):
        # print(i, data, 'fetchall')
        self.cursor.execute(self.commands[i], data)
        self.data = self.cursor.fetchall()
        return self.data

    def fetchone(self, i, data):
        # print(i, data, 'fetchone')
        self.cursor.execute(self.commands[i], data)
        self.data = self.cursor.fetchone()
        return self.data

    def execute(self, i, data):
        # print(i, data, 'execute')
        try:
            print(self.cursor.execute(self.commands[i], data))
        except Exception as e:
            return e
        return 'crated'

    def save(self):
        self.database.commit()


class Client:

    def __init__(self, clientsocket, address):
        self.HEADERSIZE = 10
        self.clientsocket = clientsocket
        self.address = address
        self.msg = None
        self.info_list = ('log_in', 'new_acc', 'dc')

    def start(self):
        cThread = threading.Thread(target=self.get_msg)
        cThread.daemon = True
        cThread.start()

    def send(self, msg):
        msg = pickle.dumps(msg)
        msg = bytes(f"{len(msg):<{self.HEADERSIZE}}", 'utf-8') + msg
        self.clientsocket.send(msg)

    def get_msg(self):
        try:
            while True:
                full_msg = b''
                new_msg = True
                msglen = None
                while True:
                        msg = self.clientsocket.recv(16)
                        if new_msg:
                            msglen = int(msg[:self.HEADERSIZE])
                            new_msg = False
                        full_msg += msg
                        if len(full_msg) - self.HEADERSIZE == msglen:
                            self.msg = pickle.loads(full_msg[self.HEADERSIZE:])
                            new_msg = True
                            full_msg = b""
                            self.handler()
        except ConnectionResetError as e:
            print('-#-', e, '-#-')

    @staticmethod
    def bytes_to_int(data):
        by = data['bytes']
        result = 0
        for b in by:
            result = result * 256 + int(b)
        return result

    @staticmethod
    def int_to_bytes(data):
        value, length = data['value'], data['length']
        result = []
        for i in range(0, length):
            result.append(value >> (i * 8) & 0xff)
        result.reverse()
        return result

    def handler(self):
        if self.msg:
            if self.msg['info'] in self.info_list:
                if self.msg['info'] == 'new_acc':
                    self.new_acc()
                if self.msg['info'] == 'log_in':
                    self.log_in()

    def new_acc(self):
        mail, pwd, name = self.msg['data']
        pwd = Hashlib.start_pass(pwd['data'])
        name, mail = name['data'], mail['data']
        max_id = data_base.where('get-max(id)', None)
        if max_id:
            max_id = int(max_id[0][0]) + 1
        else:
            max_id = 0
        data_base.execute('new_acc', (max_id, name, mail, pwd, 0))
        data_base.save()

    def log_in(self):
        mail, pwd = self.msg['data']
        pwd = Hashlib.start_pass(pwd['data'])
        pwd_data_base = ''
        try:
            pwd_data_base = data_base.fetchall('where_mail_p', (mail['data'],))[0][0]
        except Exception as e:
            print(e)
            self.send({'data': False})
        if pwd != pwd_data_base:
            self.send({'data': False})
        else:
            if pwd == pwd_data_base:
                self.send({'data': True})


class Connection:
    def __init__(self):
        self.version = 0
        self.HEADERSIZE = 10
        self.HOST = '127.0.0.1'
        self.PORT = 62914
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.HOST, self.PORT))
        self.s.listen(0)
        self.con_list = []
        print(f"online ; HOST:{self.HOST}, PORT:{self.PORT}")
        self.get_con()

    def get_con(self):
        while True:
            clientsocket, address = self.s.accept()
            print(address, 'new con')
            try:
                msg = self.get_msg(clientsocket)
                if msg['version'] != self.version:
                    file = open('data/lau.zip', 'rb')
                    data = file.read()
                    data = {'had': False, 'zip': data}
                    data = pickle.dumps(data)
                    data = bytes(f"{len(data):<{self.HEADERSIZE}}", 'utf-8') + data
                    clientsocket.send(data)
                else:
                    data = {'had': True}
                    data = pickle.dumps(data)
                    data = bytes(f"{len(data):<{self.HEADERSIZE}}", 'utf-8') + data
                    clientsocket.send(data)
                c = Client(clientsocket, address)
                self.con_list.append(c)
                thread = threading.Thread(target=c.start)
                thread.start()
            except Exception as e:
                print(e)
                clientsocket.close()

    def get_msg(self, clientsocket):
        full_msg = b''
        new_msg = True
        msglen = None
        while True:
            msg = clientsocket.recv(16)
            if new_msg:
                msglen = int(msg[:self.HEADERSIZE])
                new_msg = False
            full_msg += msg
            if len(full_msg) - self.HEADERSIZE == msglen:
                return pickle.loads(full_msg[self.HEADERSIZE:])


if __name__ == '__main__':
    try:
        data_base = DataSQL()
        server = Connection()
    except Exception as e:
        print(e)

