from flask import Flask, request, jsonify

app = Flask(__name__)

# Base de dados fake
produtos = [
    {
        "id": 1,
        "productName": "Notebook Dell",
        "productDescription": "Intel Core i5, 8GB RAM",
        "price": 3500,
        "imageUrl": ["https://via.placeholder.com/150"]
    },
    {
        "id": 2,
        "productName": "Mouse Gamer",
        "productDescription": "RGB, 6 botões",
        "price": 150,
        "imageUrl": ["https://via.placeholder.com/150"]
    }
]

@app.route("/products/search")
def search_product():
    name = request.args.get("name", "").lower()
    resultado = [p for p in produtos if name in p["productName"].lower()]
    return jsonify(resultado)

@app.route("/products/<int:product_id>")
def get_product(product_id):
    for p in produtos:
        if p["id"] == product_id:
            return jsonify([p])
    return jsonify([]), 404

@app.route("/products/add", methods=["POST"])
def add_product():
    data = request.json

    if not all(k in data for k in ("productName", "productDescription", "price", "imageUrl")):
        return jsonify({"error": "Campos obrigatórios faltando."}), 400

    novo_id = max([p["id"] for p in produtos], default=0) + 1
    produto = {
        "id": novo_id,
        "productName": data["productName"],
        "productDescription": data["productDescription"],
        "price": data["price"],
        "imageUrl": data["imageUrl"]
    }

    produtos.append(produto)
    return jsonify(produto), 201

if __name__ == "__main__":
    app.run(port=8080)
