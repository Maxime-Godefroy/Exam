class ParkingLot:
    def __init__(self, id):
        self.id = id
        self.spaces = {f"{chr(65+i)}{j}": None for i in range(5) for j in range(1, 6)}
        self.history = []

    def find_space(self, vehicle_type):
        type_to_zone = {
            'moto': 'A', 'voiture': 'B', 'voiture electrique': 'C',
            'camion/bus': 'D', 'handicapé': 'E'
        }
        zone_prefix = type_to_zone[vehicle_type]
        for key in self.spaces:
            if key.startswith(zone_prefix) and self.spaces[key] is None:
                return key
        return None

    def add_to_history(self, record):
        self.history.append(record)


class Ticket:
    def __init__(self, vehicle_plate, vehicle_type, space_id):
        self.vehicle_plate = vehicle_plate
        self.vehicle_type = vehicle_type
        self.space_id = space_id
        self.paid = False
        self.price = {'moto': 3, 'voiture': 10, 'voiture electrique': 5,
                      'camion/bus': 15, 'handicapé': 1}[vehicle_type]

    def pay(self):
        self.paid = True
