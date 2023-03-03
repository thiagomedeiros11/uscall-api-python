import zeep
from zeep import Client
from requests import Session
from zeep.transports import Transport

session = Session()
session.verify = False

url = 'http://172.20.0.3/aplicativos/webservice/wsuscall.php?wsdl'
token = '<token>'
ramal = '4306'
client = zeep.Client(url, transport=Transport(session=session))
result = client.service.getExtens(token, ramal)
print(result)

