import mysql.connector
from flask import jsonify, request, Flask
import hashlib
app = Flask(__name__)


class DataSQL:
	commands = {'new_acc': 'INSERT INTO launcher.user_acc (id, name, mail, pwd , isadmin) VALUES ( 0,%s, %s, %s, 0)'
				, 'select_all': 'SELECT * FROM launcher.use_acc'
				, 'select_name': 'SELECT name FROM launcher.user_acc'
				, 'select_mail': 'SELECT mail FROM launcher.user_acc'
				, 'select_pwd': 'SELECT pwd FROM launcher.user_acc'
				, 'where_name': 'SELECT * FROM launcher.user_acc WHERE name = s%'
				, 'where_mail': 'SELECT * FROM launcher.user_acc WHERE mail = s%'
				, 'where_mail_p': 'SELECT pwd FROM launcher.user_acc WHERE mail = s%'
				, 'where_pwd': 'SELECT * FROM launcher.user_acc WHERE pwd = s%'
				, 'update_pwd_mail': 'UPDATE launcher.user_acc SET pwd= s% WHERE mail= s%'
				, 'update_pwd_name': 'UPDATE launcher.user_acc SET pwd= s% WHERE name= s%'}

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
		self.cursor.execute(self.commands[i], data)
		self.data = self.cursor.fetchall()
		return self.data

	def fetchall(self, i, data):
		self.cursor.execute(i, data)
		self.data = self.cursor.fetchall()
		return self.data

	def execute(self, i, data):
		try:
			print(self.cursor.execute(self.commands[i], data))
		except Exception as e:
			return e
		return 'crated'

	def save(self):
		self.database.commit()


@app.route('/', methods=['POST'])
def test():
	return 'in'


@app.route('/login', methods=['POST'])
def login(massage):
	mail, pwd = massage
	pwd_sev = database.fetchall('where_mail_p', mail)
	database.save()
	if pwd_sev == hashlib_data(pwd):
		return 'in'
	else:
		return 'not'


@app.route('/new', methods=['POST'])
def new(massage):
	name, mail, pwd = massage
	print(massage)
	e = database.execute('new_acc', (name, mail, hashlib_data(pwd)))
	database.save()
	return e


def hashlib_data(data):
	data = bytes(data, 'utf-8')
	has.update(data)
	return data


if __name__ == '__main__':
	has = hashlib.sha512()
	database = DataSQL()

	#print(database.execute('new_acc', ('test', 'test@test', hashlib_data('test123'))))
	app.run(host='127.0.0.1', debug=False, port=4456)
