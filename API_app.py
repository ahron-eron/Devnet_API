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


# ---------- Andres: POST endpoint ----------
# (replace this line with your code guys)


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
