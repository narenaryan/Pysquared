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
        return res_schema.json()
    #
    # Pass a dictionary of attributes like {'FirstName':'Roger', 'LastName':'Federer', 'EmailAddress': 'rf@gmail.com'}
    #
    
    def create_lead(self,attr):
        create_lead_url = self.end_point + 'LeadManagement.svc/Lead.Create?accessKey=' +\
         self.lead_squared_access_key + '&secretKey=' + self.lead_squared_secret_key
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        json_data = json.dumps([{'Attribute' : k, 'Value': v} for k,v in attr.items()])
        res = requests.post(create_lead_url, data = json_data, headers = headers).json()
        return res

    def activity_types(self):
        activity_url = self.end_point +  '/ProspectActivity.svc/ActivityTypes.Get'
        payload = {'accessKey': self.lead_squared_access_key,'secretKey': self.lead_squared_secret_key}
        res_schema = requests.get(activity_url, params = payload)
        return res_schema.json()

    def get_lead(self,ph_no):
        lead_url = 'https://api.leadsquared.com/v2/LeadManagement.svc/Leads.Get?accessKey=%s&secretKey=%s'%(self.lead_squared_access_key,self.lead_squared_secret_key)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        dic = {  
                "Parameter": {
                    "LookupName": "Phone",
                    "LookupValue": ph_no,
                },
                "Columns": {
                    "Include_CSV": "ProspectID, FirstName, LastName, EmailAddress"
                },
                "Sorting": {
                    "ColumnName": "CreatedOn",
                    "Direction": "1"
                },
                "Paging": {
                    "PageIndex": 1,
                    "PageSize": 100
                }
        }
        res = requests.post(lead_url, data = json.dumps(dic), headers = headers).json()
        if not res:
            lead = self.create_lead({'FirstName': ph_no, 'Phone' : ph_no})
            return lead
        return res 
