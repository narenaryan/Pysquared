import requests,json

class PySquared(object):
    
    def __init__(self, lead_squared_access_key, lead_squared_secret_key):   
        # Creates a LeadSquared client object. Create object using Pysquared.PySquared("access_key", "secret_key")
        self.end_point =  'https://api.leadsquared.com/v2/'
        self.lead_squared_access_key = lead_squared_access_key  
        self.lead_squared_secret_key = lead_squared_secret_key 

    def schema(self):
        schema_url = self.end_point + 'LeadManagement.svc/LeadsMetaData.Get'
        payload = {'accessKey': self.lead_squared_access_key,'secretKey': self.lead_squared_secret_key}
        res_schema = requests.get(schema_url, params = payload) 
        return res_schema.json()

    def create_lead(self, attr):
        """
        creates leads using attribute dictionary. Ex: {'FirstName':'Naren','LastName':'Aryan'}    
        """
        create_lead_url = self.end_point + 'LeadManagement.svc/Lead.Create?accessKey=' +\
         self.lead_squared_access_key + '&secretKey=' + self.lead_squared_secret_key
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        json_data = json.dumps([{'Attribute' : k, 'Value': v} for k,v in attr.items()])
        res = requests.post(create_lead_url, data = json_data, headers = headers).json()
        return res

    def create_task(self, name, body, lead_id):
        """
        creates Tasks using attribute dictionary. Ex: {'FirstName':'Naren','LastName':'Aryan'}    
        """
        create_task_url = self.end_point +  'Task.svc/Create?accessKey=' +\
         self.lead_squared_access_key + '&secretKey=' + self.lead_squared_secret_key
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        json_data = json.dumps({
              "Name": name,
              "RelatedEntity" : 0,
              "Description": body,
              "RelatedEntityId": lead_id,
            })
        res = requests.post(create_task_url, data = json_data, headers = headers).json()
        return res

    def activity_types(self):
        activity_url = self.end_point +  '/ProspectActivity.svc/ActivityTypes.Get'
        payload = {'accessKey': self.lead_squared_access_key,'secretKey': self.lead_squared_secret_key}
        res_schema = requests.get(activity_url, params = payload)
        return res_schema.json()

    def get_lead(self,ph_no):
        """
        :gets details about a phone number. It creates one if not existing.
        """
        lead_url = 'https://api.leadsquared.com/v2/LeadManagement.svc/Leads.Get?accessKey=%s&secretKey=%s'%(self.lead_squared_access_key,self.lead_squared_secret_key)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        dic = {  
                "Parameter": {
                    "LookupName": "Phone",
                    "LookupValue": ph_no,
                },
                "Columns": {
                    #"Include_CSV": "ProspectID, FirstName, LastName, EmailAddress"   ## Adding more fields below
                    "Include_CSV": "ProspectID, FirstName, LastName, EmailAddress, CreatedByName"
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


    def daily_leads(self, date, pg_no):
        """
        :get a dump of all leads created on a particular day. Paginate the results using Page Number parameter for multiple calls
        """
        lead_url = 'https://api.leadsquared.com/v2/LeadManagement.svc/Leads.Get?accessKey=%s&secretKey=%s'%(self.lead_squared_access_key,self.lead_squared_secret_key)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        dic = {  
                "Parameter": {
                    "LookupName": "CreatedOn",
                    "LookupValue": date,
                },
                "Columns": {
                    #"Include_CSV": "ProspectID, FirstName, LastName, EmailAddress"   ## Adding more fields below
                    "Include_CSV": "ProspectID, FirstName, LastName, EmailAddress, CreatedByName, Phone"
                },
                "Sorting": {
                    "ColumnName": "CreatedOn",
                    "Direction": "1"
                },
                "Paging": {
                    "PageIndex": pg_no,
                    "PageSize": 1000
                }
        }
        res = requests.post(lead_url, data = json.dumps(dic), headers = headers).json()
        if not res:
            lead = self.create_lead({'FirstName': ph_no, 'Phone' : ph_no})
            return lead
        return res 
