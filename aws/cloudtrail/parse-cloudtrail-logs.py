import gzip
import json
import os.path

sbx = []
preprod = []
prod = []
gpdb_hosts = []

logs = [name for name in os.listdir(os.getcwd())
        if os.path.isfile(os.path.join(os.getcwd(), name))]

for log in logs:
    if log.endswith('json.gz'):

        with gzip.open(log, 'r') as f:        
            data = json.loads(f.read())

        for event in data['Records']:
           if event['sourceIPAddress'] in prod and event['eventTime'] == '2019-01-13T05:43:21Z':
                print('userIdentity: {0}'.format(event['userIdentity']))
                print('additionalEventData: {0}'.format(event['additionalEventData']))
                print('requestParameters: {0}'.format(event['requestParameters']))
                print('sourceIPAddress: {0}'.format(event['sourceIPAddress']))
                print('responseElements: {0}'.format(event['responseElements'])) #None
                print('requestID: {0}'.format(event['requestID']))
                print('eventID: {0}'.format(event['eventID']))
                print('eventTime: {0}'.format(event['eventTime']))
                print(end='\n')
                #print(event)
                ###print(event['additionalEventData']) # x-amz-id-2 key/value
                ###print(event['additionalEventData']['x-amz-id-2']) # x-amz-id-2 key/value
                ###print(event['errorCode'])
                ###print(event['errorMessage'])
                ###print(event['eventID']) 
                ###print(event['eventTime']) 
                ###print(event['eventType']) 
                ###print(event['recipientAccountId']) 
                ###print(event['requestID']) 
                ###print(event['requestParameters']['bucketName']) 
                ###print(event['requestParameters']['key']) 