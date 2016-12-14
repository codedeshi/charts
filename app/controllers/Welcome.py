from system.core.controller import *

class Welcome(Controller):
	def __init__(self, action):
		super(Welcome, self).__init__(action)
		self.load_model('WelcomeModel')


	def index(self):
		session['user'] = None
		return self.load_view('index.html')

	def registration(self):
		data = {
			'name': request.form['name'],
			'uname': request.form['uname'],
			'password': request.form['password'],
			'confirm': request.form['confirm']
		}        
		reg_status = self.models['WelcomeModel'].register(data)
		if reg_status['status'] == True:
			session['user']= reg_status['user_id']
			return redirect("/charts")
		else:
			print reg_status['error']
			for messages in reg_status['error']:
				flash(messages)
			return redirect("/")

	def login(self):
		data = {
			'uname': request.form['uname'],
			'password': request.form['password']
		}
		for i in data:
			if len(data[i])<1:
				flash("Please put a valid username and password")
				return redirect('/')
				
		log_status = self.models['WelcomeModel'].login(data)        
		if log_status == False:
			flash("Please put a valid username and password")
			return redirect('/')
		else:            
			session['user'] = log_status['id']
			return redirect('/charts')

	def logoff(self):
		session['user'] = None
		return redirect("/")



