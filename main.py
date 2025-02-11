import json

def write_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def read_from_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

class Reservation:
    def __init__(self, client_name, transport, ticket, schedule=None):
        self.client_name = client_name
        self.transport = transport
        self.ticket = ticket
        self.schedule = schedule
class Ticket:
    def __init__(self, client_name, transport, schedule):
        self.client_name = client_name
        self.transport = transport
        self.schedule = schedule

class Transport:
    def __init__(self, transport_type, capacity, schedule):
        self.transport_type = transport_type
        self.capacity = capacity
        self.available_seats = capacity
        self.schedule = schedule

    def book_seat(self):
        if self.available_seats > 0:
            self.available_seats -= 1 #уменьшаем при брони доступные места
            return True
        return False

class Client:
    def __init__(self, name):
        self.name = name


class TransportManager:
    def __init__(self):
        self.transports = []

class TicketManager:
    def __init__(self):
        self.tickets = []
    def create_ticket(self, client_name, transport, schedule):
        ticket = Ticket(client_name, transport, schedule)
        return ticket
    def add_ticket(self, ticket):
        self.tickets.append(ticket)

class ReservationManager:
    def __init__(self):
        self.reservations = []

    def create_reservation(self, client_name, transport, ticket, schedule):
        reservation = Reservation(client_name, transport, ticket, schedule)
        self.reservations.append(reservation)
        return reservation

class Notification:
    def __init__(self):
        self.notifications = []

    def send_notification(self, client_name, message):
        notification = f"Уведомление для {client_name}: {message}"
        self.notifications.append(notification)
        print(notification)

    def show_notifications(self):
        if not self.notifications:
            print("Нет уведомлений.")
        else:
            for notification in self.notifications:
                print(notification)
class BookingSystem:
    def __init__(self):
        self.transports = []
        self.ticket_manager = TicketManager()
        self.reservation_manager = ReservationManager()
        self.notification_manager = Notification()

    def add_transport(self, transport_type, capacity, schedule):
        new_transport = Transport(transport_type, capacity, schedule)
        self.transports.append(new_transport)
        print(f"Добавлен транспорт: {transport_type} с {capacity} местами.")
        return new_transport

    def show_schedule(self, transport_type):
        for t in self.transports:
            if t.transport_type == transport_type:
                print(f"Расписание для {transport_type}:")
                for dep, arr in t.schedule:
                    print(f"{dep} - {arr}")
                return
        print(f"Транспорт {transport_type} не найден.")
    def book_ticket(self, client, transport_type, departure_time, schedule=None):
        transport = None
        for t in self.transports:
            if t.transport_type == transport_type:
                transport = t
                break

        if transport is None:
            print(f"Транспорт {transport_type} не найден.")
            return

        if not transport.book_seat():
            print(f"Нет свободных мест на {transport_type}.")
            return
        schedule = None
        for dep, arr in transport.schedule:
            if dep == departure_time:
                schedule = (dep, arr)
                break

        if schedule is None:
            print(f"Нет доступных рейсов на {departure_time}.")
            return
        ticket = self.ticket_manager.create_ticket(client.name, transport, schedule)
        self.ticket_manager.add_ticket(ticket)

        # Создаём бронирование
        reservation = self.reservation_manager.create_reservation(client.name, transport, ticket, schedule)
        self.notification_manager.send_notification(client.name,f"Билет на {transport_type} успешно куплен. Время отправления: {departure_time}")


def menu():
    system = BookingSystem()
    bus_schedule = [("10:00", "12:00"), ("14:00", "16:00")]
    train_schedule = [("15:00", "18:00"), ("19:00", "22:00")]

    bus = system.add_transport("Автобус", 10, bus_schedule)
    train = system.add_transport("Поезд", 50, train_schedule)
    transport_type = input("Введите тип транспорта для просмотра расписания: ")
    system.show_schedule(transport_type)
    client_name = input("Введите имя клиента: ")
    client = Client(client_name)
    transport_type = input("Введите тип транспорта для покупки билета: ")
    departure_time = input("Выберите время отправления: ")
    system.book_ticket(client, transport_type, departure_time)

    system.notification_manager.show_notifications()
menu()
data = {
    "Transports": [
        {"Type": "Автобус", "Capacity": 10, "Schedule": [{"Departure": "10:00", "Arrival": "12:00"}, {"Departure": "14:00", "Arrival": "16:00"}]},
        {"Type": "Поезд", "Capacity": 50, "Schedule": [{"Departure": "15:00", "Arrival": "18:00"}, {"Departure": "19:00", "Arrival": "22:00"}]}
    ],
    "Clients": [
        {"Name": "Соня"},
        {"Name": "Лука"}
    ]
}
write_to_json(data, 'data.json')
json_data = read_from_json('data.json')
print(json_data)