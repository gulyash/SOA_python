from xmlrpc.server import SimpleXMLRPCServer


def my_first_service():
    return "Hello world!"


def service_args(*args):
    return f"Received arguments: {args}"


server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(my_first_service)
server.register_function(service_args, "service_args")
server.serve_forever()
