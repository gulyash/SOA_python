from http.server import HTTPServer

from pysimplesoap.server import SoapDispatcher, SOAPHandler, unicode

dispatcher = SoapDispatcher(
    'SOAServer',
    location="http://localhost:8050/",
    action='http://localhost:8050/',  # SOAPAction
    namespace="http://example.com/sample.wsdl", prefix="ns0",
    trace=True,
    ns=True)


def my_first_service(request):
    return "Hello world!"


def service_args(arg1, arg2, arg3):
    return f"Received arguments: {arg1}, {arg2} and  {arg3}"


# register the user function
dispatcher.register_function('MyFirstService', my_first_service,
                             returns={'result': unicode})
dispatcher.register_function('MyArgsService', service_args,
                             returns={'result': unicode}, args={'arg1': unicode,
                                                                'arg2': unicode,
                                                                'arg3': unicode})

print("Starting server...")
httpd = HTTPServer(("", 8050), SOAPHandler)
httpd.dispatcher = dispatcher
httpd.serve_forever()
