import requests,json

class PySquared(object):
	
	def __init__(self, lead_squared_access_key, lead_squared_secret_key):
		self.end_point =  'https://api.leadsquared.com/v2/'
		self.lead_squared_access_key = lead_squared_access_key
		self.lead_squared_secret_key = lead_squared_secret_key

	def schema(self):
		schema_url = self.end_point + 'LeadManagement.svc/LeadsMetaData.Get'
		payload = {'accessKey': self.lead_squared_access_key,'secretKey': self.lead_squared_secret_key}
		res_schema = requests.get(schema_url, params = payload) 
		return res_schema
	#
	# Pass a dictionary of attributes like {'FirstName':'Roger', 'LastName':'Federer', 'EmailAddress': 'rf@gmail.com'}
	#
	def create_lead(self,attr):
	    create_lead_url = self.end_point + 'LeadManagement.svc/Lead.Create?accessKey=' +\
		 self.lead_squared_access_key + '&secretKey=' + self.lead_squared_secret_key
		headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
		json_data = [{'Attribute' : k, 'Value': v} for k,v in attr.values()]


l = PySquared('u$r075de1e5561edbc1181e757698a32f0b', 'cb9ea1d8492e93d7684d99e20625fb8692f982c2')

