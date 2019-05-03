import os
from flask import Flask, request
import http.client
app = Flask(__name__)
@app.route('/')
def client():
    host = os.getenv("SERVERSERVICE_SERVICE_HOST")
    port = os.getenv("SERVERSERVICE_SERVICE_PORT")
    backend_connect = http.client.HTTPConnection(host, port)
    #you can params and headers also here just specify the method, url
    backend_connect.request("GET", "/")
    response = backend_connect.getresponse()
    return response.read()
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
