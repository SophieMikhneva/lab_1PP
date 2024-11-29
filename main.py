class Schedule:
    def __init__(self):
        self.schedules = []
class Reservation:
    def __init__(self, customer_name, transport, ticket, schedule=None):
        self.customer_name = customer_name
        self.transport = transport
        self.ticket = ticket
        self.schedule = schedule
class Ticket:
    def __init__(self, customer_name, transport, price, schedule):
        self.customer_name = customer_name
        self.transport = transport
        self.price = price
        self.schedule = schedule
        self.is_paid = False
class Pay:
    def __init__(self, passenger_name, amount):
        self.passenger_name = passenger_name
        self.amount = amount

class Transport:
    def __init__(self, transport_type, capacity):
        self.transport_type = transport_type
        self.capacity = capacity
        self.available_seats = capacity
        self.schedule = []
class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
class TransportManager:
    def __init__(self):
        self.transports = []
        self.schedule = Schedule()
class TicketManager:
    def __init__(self):
        self.tickets = []
class ReservationManager:
    def __init__(self):
        self.reservations = []

class BookingSystem:
    def __init__(self):
        self.transport_manager = TransportManager()
        self.ticket_manager = TicketManager()
        self.reservation_manager = ReservationManager()
