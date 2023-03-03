# suds is a lightweight SOAP-based web service client for Python licensed under LGPL
# https://github.com/suds-community/suds

from suds.client import *
import ssl
import urllib3
# import logging
# logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
from suds.xsd.doctor import ImportDoctor, Import



# url de integração
url = 'http://172.20.0.3/aplicativos/webservice/wsuscall.php?wsdl'

imp = Import('http://schemas.xmlsoap.org/soap/encoding/')
imp.filter.add('http://schemas.xmlsoap.org/wsdl/')
doctor = ImportDoctor(imp)

client = Client(url, doctor=doctor)


# approach to turn off certificate validation in suds is to use a custom transport class. For example in Python 3:

class UnverifiedHttpsTransport(suds.transport.http.HttpTransport):
    def __init__(self, *args, **kwargs):
        super(UnverifiedHttpsTransport, self).__init__(*args, **kwargs)

    def u2handlers(self):
        handlers = super(UnverifiedHttpsTransport, self).u2handlers()
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        handlers.append(urllib.request.HTTPSHandler(context=context))
        return handlers


# classe com as funcoes
class funcoes():

    def startCall():
        key = '<token>'  
        tipo = 'outbound'
        origem = '4306'                             
        destino = '1139952800'
        categoria = '1'
        client = Client(url, transport=UnverifiedHttpsTransport())
        result = client.service.startCall(key, tipo, origem, destino, categoria)
        return(result)    

    def getExtens():
        token = '<token>' 
        ramal = '4306'
        client = Client(url, transport=UnverifiedHttpsTransport())
        result = client.service.getExtens(token, ramal)
        return(result)


funcoes.getExtens()

