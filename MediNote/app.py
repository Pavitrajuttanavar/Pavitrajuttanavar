from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/save", methods=["POST"])
def save_notes():
    data = request.json
    patient_name = data.get("patient_name")
    patient_id = data.get("patient_id")
    notes = data.get("notes")

    print("Saved:", data)

    return jsonify({"message": "Notes saved successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
