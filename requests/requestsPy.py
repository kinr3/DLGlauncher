import requests


class Data(requests):

    def __init__(self, web, port):
        assert web == str()
        assert port == str()
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

    def log_in(self, mal, pwd):
        self.response = None # requests.post(self.web+':'+self.port+'/')
        return self.response

    def logged_in(self, port):
        self.response = None # requests.post(self.web+':'+self.port+'/')
        return self.response

    def get_server(self):
        self.response = None # requests.post(self.web+':'+self.port+'/')
        return self.response

    def get_game(self):
        self.response = None # requests.post(self.web+':'+self.port+'/')
        return self.response

    def get_all(self):
        self.response = None # requests.post(self.web+':'+self.port+'/')
        return self.response

    def get_friends(self):
        self.response = None # requests.post(self.web+':'+self.port+'/')
        return self.response

    def get_updates(self):
        self.response = None # requests.post(self.web+':'+self.port+'/')
        return self.response

    def add_friends(self):
        self.response = None # requests.post(self.web+':'+self.port+'/')
        return self.response
