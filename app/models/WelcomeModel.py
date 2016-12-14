from system.core.model import Model

class WelcomeModel(Model):
	def __init__(self):
		super(WelcomeModel, self).__init__()

	def register(self, data):
		error = []

		if len(data['name']) < 3:
			error.append("Name should be atleast 3 characters")
		if len(data['uname']) < 3:
			error.append("User name should be atleast 3 characters")
		if len(data['password']) < 8:
			error.append("Password should be atleast 8 characters")
		if data['password'] != data['confirm']:
			error.append('Password and confirm pw should match')

		if error:
			return {'status': False , 'error': error}
		else:
			try:
				query = "INSERT into users (name, uname,password) values (:name, :uname, :password)"
				data['password'] = self.bcrypt.generate_password_hash(data['password'])
				user_id = self.db.query_db(query, data)        
				return {'status': True, "user_id": user_id}
			except Exception as e:
				error.append(str(e))
				return {'status': False , 'error': error}

	def login(self,data):
		query = "SELECT * from users where uname=:uname"
		query_data = {
			'uname': data['uname'],                
		}
		user_data = self.db.query_db(query, query_data)
		if len(user_data)==1:
			if self.bcrypt.check_password_hash(user_data[0]['password'], data['password']):
				print 'pass'
				return user_data[0]

			else:
				print "Failed"
				return False
		return False



