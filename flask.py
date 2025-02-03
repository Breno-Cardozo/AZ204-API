from flask import Flask, request, jsonify

app = Flask(__name__)

def index():
    return jsonify({"message": "API Flask rodando com sucesso!"})

@app.route("/add", methods=["POST"])
def add_data():
    try:
        data = request.get_json()
        return jsonify({"message": "Dados recebidos", "data": data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/data", methods=["GET"])
def get_data():
    sample_data = {"id": 1, "nome": "Exemplo", "descricao": "Este é um exemplo de API Flask"}
    return jsonify(sample_data)

if __name__ == "__main__":
    app.run(debug=True)
