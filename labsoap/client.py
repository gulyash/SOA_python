from zeep import Client

client = Client(wsdl="ws.wsdl")

r1 = client.service.MyFirstService()
print(r1)
r2 = client.service.MyArgsService('kek', 'lol', 'azaza')
print(r2)
