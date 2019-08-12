import requests
from flask import jsonify


class Data:

    def __init__(self, web, port):
        self.error = 'Connected'
        self.response = None
        self.web = web
        self.port = port
        try:
            self.key = requests.post(web+':'+port+'/')
        except Exception as e:
            self.error = e, 'Connection failed'
        super(Data, self).__init__()
        self.first_start()

    def first_start(self):
        return self.error

    def new_acc(self, name, mail, pwd):
        massage = jsonify([name, mail, pwd])
        print(massage)
        self.response = requests.post(self.web+':'+self.port+'/new', json=massage) #json,parameters
        return self.response

    def log_in(self, mail, pwd):
        massage = [{'mail': mail, 'pwd': pwd}]
        self.response = requests.post(self.web + ':' + self.port + '/login', json=massage)
        return self.response

    def logged_in(self, port):
        self.response = None # py_lau_scripts.post(self.web+':'+self.port+'/')
        return self.response.json()

    def get_server(self):
        self.response = None # py_lau_scripts.post(self.web+':'+self.port+'/')
        return self.response.json()

    def get_game(self):
        self.response = None # py_lau_scripts.post(self.web+':'+self.port+'/')
        return self.response.json()

    def get_all(self):
        self.response = None # py_lau_scripts.post(self.web+':'+self.port+'/')
        return self.response.json()

    def get_friends(self):
        self.response = None # py_lau_scripts.post(self.web+':'+self.port+'/')
        return self.response.json()

    def get_updates(self):
        self.response = None # py_lau_scripts.post(self.web+':'+self.port+'/')
        return self.response.json()

    def add_friends(self):
        self.response = None # py_lau_scripts.post(self.web+':'+self.port+'/')
        return self.response.json()
