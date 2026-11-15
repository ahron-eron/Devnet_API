from flask import Flask, jsonify, request

app = Flask(__name__)

# our "database" is just a list
devices = [
    {"device_id": 1, "owner": "Room 1 - eron", "status": "disconnected"},
    {"device_id": 2, "owner": "Room 3 - erown", "status": "connected"}
]
next_id = 3


# ---------- Kurt: GET endpoints ----------
# (replace this line with your code guys)
# get all devices
@app.route("/devices", method=["GET"])
def get_devices():
    return jsonify(devices), 200

# get one device by id
@app.route("/devices/<int:device_id>", method=["GET"])
def get_device(device_id):
    for d in devices:
        if d["device_id"] == device_id:
            return jsonify(d), 200
    return jsonify({"error": "Device not found"}), 404

# ---------- Andres: POST endpoint ----------
# (replace this line with your code guys)
# update the status of a device
@app.route("/devices/<int:device_id>", methods=["PUT"])
def update_device(device_id):
    data = request.get_json()

    for d in devices:
        if d["device_id"] == device_id:
            if data is None or "status" not in data:
                return jsonify({"error": "status is required"}), 400

            if data["status"] != "connected" and data["status"] != "disconnected":
                return jsonify({"error": "status must be connected or disconnected"}), 400

            d["status"] = data["status"]
            return jsonify(d), 200

    return jsonify({"error": "Device not found"}), 404


# ---------- Jaynard: PUT endpoint ----------
# (replace this line with your code guys)


# delete a device
@app.route("/devices/<int:device_id>", methods=["DELETE"])
def delete_device(device_id):
    for d in devices:
        if d["device_id"] == device_id:
            devices.remove(d)
            return jsonify({"message": "Device deleted"}), 200
    return jsonify({"error": "Device not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
