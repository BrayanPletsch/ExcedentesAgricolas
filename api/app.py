from flask import Flask, request, jsonify
from flask_cors import CORS
from services.ong_service import OngService
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from http.server import BaseHTTPRequestHandler

app = Flask(__name__)
CORS(app)
ong_service = OngService()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/search', methods=['GET'])
def search_ongs():
    query = request.args.get('q', '')
    results = ong_service.search_ongs(query)
    return jsonify(results)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Passa as requisições para o app Flask
        app_wsgi = DispatcherMiddleware(app)
        environ = {
            'wsgi.url_scheme': 'http',
            'REQUEST_METHOD': self.command,
            'PATH_INFO': self.path,
            'QUERY_STRING': '',
        }
        headers = {key.lower(): value for key, value in self.headers.items()}
        environ.update({f'HTTP_{key.upper()}': value for key, value in headers.items()})
        start_response = lambda status, response_headers: self.send_response(int(status.split(' ')[0]))
        result = app_wsgi(environ, start_response)
        for data in result:
            self.wfile.write(data)

if __name__ == '__main__':
    app.run(debug=True)