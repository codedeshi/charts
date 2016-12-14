from system.core.controller import *

class Stock(Controller):
	def __init__(self, action):
		super(Stock, self).__init__(action)
		self.load_model('StockModel')

	def charts(self):
		if session['user'] == None:
			return redirect('/')
		else:
			stock_list = self.models['StockModel'].get_stock_list()
			return self.load_view('chart.html',stock_list=stock_list)

	def stock(self):
		if session['user'] == None:
			return redirect('/')
		else:
			params = {
				'code': request.form['code'],
				'start_date': request.form['start_date'],
				'end_date': request.form['end_date']
			}
			data = self.models['StockModel'].get_data(params)
			return jsonify(data=data)