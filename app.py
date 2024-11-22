from flask import Flask, request, jsonify
from flask_cors import CORS
from services.ong_service import OngService

app = Flask(__name__)
CORS(app)  # Permite requisições de qualquer origem (global)
ong_service = OngService()

@app.route('/search', methods=['GET'])
def search_ongs():
    query = request.args.get('q', '')
    results = ong_service.search_ongs(query)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
