class Seat:
    def __init__(self, seat_number, seat_type):
        self.seat_number = seat_number  # Номер места
        self.seat_type = seat_type  # Тип места (например, стандартное, бизнес)
        self.is_booked = False
class Schedule:
    def __init__(self):
        self.schedule = []
class Pay:
    def __init__(self, passenger_name, amount):
        self.passenger_name = passenger_name
        self.amount = amount
class PassengerProfile:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class Passenger:
    def __init__(self, name, email, phone):
        self.name = name
        self.profile = PassengerProfile(name, email, phone)
        self.history = BookingHistory()
        self.notifications = Notification(name)
class BookingHistory:
    def __init__(self):
        self.history = []
class Transport:
    def __init__(self, type_of_transport, route, total_seats, ticket_price, seat_type="Стандарт"):
        self.type_of_transport = type_of_transport  # Тип транспорта
        self.route = route  # Маршрут
        self.total_seats = total_seats  # Всего мест
        self.ticket_price = ticket_price  # Цена билета
        self.seat_type = seat_type  # Тип мест (например, стандартные или бизнес-класс)
        self.booked_seats = 0  # Забронированные места
        self.seats = [Seat(seat_number=i+1, seat_type=seat_type) for i in range(total_seats)]  # Список мест

class Notification:
    def __init__(self, passenger_name):
        self.passenger_name = passenger_name
class BookingSystem:
    def __init__(self):
        self.transports = []
        self.schedule = Schedule()