from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from sklearn.ensemble import IsolationForest
import numpy as np
import datetime

app = Flask(__name__)
CORS(app)

# --- Model AI sederhana (deteksi anomali) ---
data_normal = np.array([
    [70, 98], [72, 97], [80, 96], [65, 99], [78, 97]
])
model = IsolationForest(contamination=0.15, random_state=42)
model.fit(data_normal)

# Data terakhir yang diterima dari ESP32
last_data = {
    "bpm": 0,
    "spo2": 0,
    "status": "Menunggu data...",
    "ts": None
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data", methods=["POST"])
def receive_data():
    global last_data
    content = request.get_json(force=True)

    bpm = float(content.get("bpm", 0))
    spo2 = float(content.get("spo2", 0))

    # Prediksi normal / anomali dengan IsolationForest
    sample = np.array([[bpm, spo2]])
    pred = model.predict(sample)[0]
    status = "Normal" if pred == 1 else "Anomali"

    last_data = {
        "bpm": bpm,
        "spo2": spo2,
        "status": status,
        "ts": datetime.datetime.utcnow().isoformat() + "Z"
    }

    print("📥 Data diterima:", last_data)
    return jsonify(last_data)

@app.route("/latest")
def latest():
    return jsonify(last_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
