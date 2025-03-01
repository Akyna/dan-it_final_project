from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def health_check():
    return "Test ArgoCD - attempt 5", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
