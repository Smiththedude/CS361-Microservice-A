from flask import Flask, jsonify, request
import json
import uuid
import os

FILE = "licenses.json"
app = Flask(__name__)

if os.path.exists(FILE):
    with open(FILE, "r") as f:
        try:
            licenses = json.load(f)
        except json.JSONDecodeError:
            licenses = {}

else:
    licenses = {}

def save_file():
    with open(FILE, "w") as f:
        json.dump(licenses, f, indent=4)

@app.route('/licenses', methods=['GET'])
def get_all():
    return jsonify(licenses)

@app.route('/licenses/<string:license_id>', methods=['GET'])
def get_license(license_id):
    for license in licenses:
        if "id" in license and license["id"] == license_id:
            with open("output.json", "w") as f:
                json.dump(license, f, indent=4)
            return jsonify(license)
    return jsonify({"error": "License not found"}), 404

@app.route('/licenses', methods=['POST'])
def add_license():
    global licenses
    new_license = request.get_json()
    if not new_license:
        return jsonify({"error": "No license data"}), 400
    if "id" not in new_license:
        new_license["id"] = str(uuid.uuid4())

    if not isinstance(licenses, list):
        licenses = []
    licenses.append(new_license)
    save_file()
    return jsonify(new_license), 201

@app.route('/licenses/<string:license_id>', methods=['DELETE'])
def delete_license(license_id):
    global licenses
    licenses = [lic for lic in licenses if lic["id"] != license_id]
    save_file()
    return jsonify({"message": f"License {license_id} deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)


