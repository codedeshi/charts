import quandl
from system.core.model import Model
import pandas as pd 
from flask import json

quandl.ApiConfig.api_key = 'HW4xKEMjuNxCZNPbEUei'

class StockModel(Model):
	def __init__(self):
		super(StockModel, self).__init__()

	def get_stock_list(self):
		query = "select code, name from stocks"
		stock_list = self.db.query_db(query)
		return stock_list

	def get_data(self,params):
		error = []
		if len(params['code'])<1:
			error.append('Name cannot be blank')
		if params['start_date'] > params['end_date']:
			error.append("Invalid date input")
		if error:
			return {'error':error}
		else:
			open = list(quandl.get(params['code'], start_date=params['start_date'],end_date=params['end_date'],column_index =8)['Adj. Open'])
			high = list(quandl.get(params['code'], start_date=params['start_date'],end_date=params['end_date'],column_index =9)['Adj. High'])
			low = list(quandl.get(params['code'], start_date=params['start_date'],end_date=params['end_date'],column_index =10)['Adj. Low'])
			close = list(quandl.get(params['code'], start_date=params['start_date'],end_date=params['end_date'],column_index =11)['Adj. Close'])
			dates = quandl.get(params['code'], start_date=params['start_date'],end_date=params['end_date'],column_index =8).index.values
			dates = [pd.to_datetime(str(date)).strftime('%Y/%m/%d') for date in dates]
			query = "select name from stocks where code=:code"
			stock_name = self.db.query_db(query,params)[0]['name']
			print stock_name
			data = {
				'name': stock_name,
				'open' : open,
				'high' : high,
				'low' : low,
				'close' : close,
				'dates' : dates
			}
			return data


