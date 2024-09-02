from flask import Flask, request, jsonify
from services import ParkingService

app = Flask(__name__)
service = ParkingService()

@app.route('/parkings', methods=['POST'])
def add_parking():
    data = request.json
    return jsonify(service.add_parking(data['parking_id']))

@app.route('/enter', methods=['POST'])
def enter_parking():
    data = request.json
    return jsonify(service.enter_parking(data['parking_id'], data['vehicle_type'], data['vehicle_plate']))

@app.route('/pay', methods=['POST'])
def pay_for_parking():
    data = request.json
    return jsonify(service.pay_for_parking(data['parking_id'], data['space_id']))

@app.route('/exit', methods=['POST'])
def exit_parking():
    data = request.json
    return jsonify(service.exit_parking(data['parking_id'], data['space_id']))

@app.route('/history/<parking_id>', methods=['GET'])
def get_history(parking_id):
    return jsonify(service.view_history(parking_id))

if __name__ == '__main__':
    app.run(debug=True)
