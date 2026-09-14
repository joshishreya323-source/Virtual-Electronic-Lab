from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Virtual Electronic Lab Backend is Running!"


# Ohm's Law API
@app.route("/ohms-law", methods=["POST"])
def ohms_law():

    data = request.get_json()

    voltage = data["voltage"]
    resistance = data["resistance"]

    current = voltage / resistance

    return jsonify({
        "voltage": voltage,
        "resistance": resistance,
        "current": current,
        "current_mA": current * 1000,
        "message": "Ohm's Law calculation successful"
    })


# Start the server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)