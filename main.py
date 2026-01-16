from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Rota para o arquivo principal
@app.route("/")
def index():
    return send_from_directory(".", "index.html")

# Rota para pastas secundárias (css, js, assets)
@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(".", path)

if __name__ == "__main__":
    # O Discloud exige que a porta seja lida da variável de ambiente
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)