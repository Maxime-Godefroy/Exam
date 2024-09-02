from models import ParkingLot, Ticket

class ParkingService:
    def __init__(self):
        self.parkings = {}

    def add_parking(self, parking_id):
        if parking_id not in self.parkings:
            self.parkings[parking_id] = ParkingLot(parking_id)
            return "Parking added"
        return "Parking already exists"

    def enter_parking(self, parking_id, vehicle_type, vehicle_plate):
        if parking_id in self.parkings:
            parking_lot = self.parkings[parking_id]
            space_id = parking_lot.find_space(vehicle_type)
            if space_id is not None:
                ticket = Ticket(vehicle_plate, vehicle_type, space_id)
                parking_lot.spaces[space_id] = ticket
                return f"Ticket issued. Space ID: {space_id}, Price: {ticket.price}"
            return "No space available"
        return "Parking not found"

    def pay_for_parking(self, parking_id, space_id):
        if parking_id in self.parkings:
            parking_lot = self.parkings[parking_id]
            ticket = parking_lot.spaces.get(space_id)
            if ticket and not ticket.paid:
                ticket.pay()
                parking_lot.add_to_history(vars(ticket))
                return "Payment successful"
            return "Ticket already paid or not found"
        return "Parking not found"

    def exit_parking(self, parking_id, space_id):
        if parking_id in self.parkings:
            parking_lot = self.parkings[parking_id]
            ticket = parking_lot.spaces.get(space_id)
            if ticket and ticket.paid:
                parking_lot.spaces[space_id] = None
                return "Exit granted"
            return "Payment required"
        return "Parking not found"

    def view_history(self, parking_id):
        if parking_id in self.parkings:
            return self.parkings[parking_id].history
        return "Parking not found"
